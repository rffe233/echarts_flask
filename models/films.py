from collections import defaultdict

from sqlalchemy import func, asc
from app import db
import re


class FilmInfo(db.Model):
    __tablename__ = 'movie_data'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(64))
    director = db.Column(db.String(64))
    language = db.Column(db.String(64))
    rate = db.Column(db.Float)
    rating_num = db.Column(db.Float)
    region = db.Column(db.String(64))
    runtime = db.Column(db.Integer)
    title = db.Column(db.String(64))
    type = db.Column(db.String(64))
    year = db.Column(db.Integer)
    is_cn = db.Column(db.Integer)
    is_hk = db.Column(db.Integer)
    is_tw = db.Column(db.Integer)
    actor = db.Column(db.String(128))

    def to_dict(self):

        return {
            'id': self.id,
            'date': self.date,
            'director': self.director,
            'language': self.language,
            'rate': self.rate,
            'rating_num': self.rating_num,
            'region': self.region,
            'runtime': self.runtime,
            'title': self.title,
            'type': self.type,
            'year': self.year,
        }

    @staticmethod
    def count_by_year():
        aresult = db.session.query(FilmInfo.year, func.count()).group_by(
            FilmInfo.year).all()  # 使用func。count（FilmInfo.id)是等价
        count_by_year_dict = {year: count for year, count in aresult}
        result = count_by_year_dict
        return result

    @staticmethod
    def ratenum_by_year():
        aresult= db.session.query(FilmInfo.year, func.avg(FilmInfo.rating_num)).group_by(FilmInfo.year).all()
        ratenum_by_year_dict = {year: count for year, count in aresult}
        result =  ratenum_by_year_dict
        return result

    @staticmethod
    def rate_by_year():
        aresult = db.session.query(FilmInfo.year, func.avg(FilmInfo.rate)).group_by(FilmInfo.year).all()
        ratenum_by_year_dict = {year: count for year, count in aresult}
        result = ratenum_by_year_dict
        return result

    @staticmethod
    def get_film_num():
        result = FilmInfo.query.count()
        return result

    @staticmethod
    def get_film_rate():
        result = {'好片': {}, '普通': {}, '烂片': ''}
        good_film = FilmInfo.query.filter(FilmInfo.rate >= 8).count()
        bad_film = FilmInfo.query.filter(FilmInfo.rate < 6).count()
        allfilm = FilmInfo.query.count()
        good_film1 = good_film / allfilm
        processed_data = "{:.2%}".format(good_film1)
        bad_film1 = bad_film / allfilm
        processed_data2= "{:.2%}".format(bad_film1)
        ordinary_film1 = 1 - bad_film1 - good_film1
        processed_data3 = "{:.2%}".format(ordinary_film1)
        result['好片'] = processed_data
        result['普通'] = processed_data3
        result['烂片'] = processed_data2
        return result

    @staticmethod
    def get_film_time():
        result = {'上世纪': {}, '世纪初': {}, '近年': ''}
        near_film = FilmInfo.query.filter(FilmInfo.year < 2000).count()
        far_film = FilmInfo.query.filter(FilmInfo.year > 2013).count()  # 好像意思写反了，，，
        allfilm = FilmInfo.query.count()
        near_film1 = near_film / allfilm
        processed_data = "{:.2%}".format(near_film1)
        far_film1 = far_film / allfilm
        processed_data2 = "{:.2%}".format(far_film1)
        ordinary_film1 = 1 - far_film1 - near_film1
        processed_data23 = "{:.2%}".format(ordinary_film1)
        result['上世纪'] = processed_data
        result['世纪初'] = processed_data2
        result['近年'] = processed_data23
        return result

    @staticmethod
    def get_film_region():
        result = {'大陆': {}, '台湾': {}, '香港': ''}
        cn_film = FilmInfo.query.filter(FilmInfo.is_cn == 1).count()
        hk_film = FilmInfo.query.filter(FilmInfo.is_hk == 1).count()
        tw_film = FilmInfo.query.filter(FilmInfo.is_tw == 1).count()
        allfilm = FilmInfo.query.count()
        cn_film1 = cn_film / allfilm
        processed_data = "{:.2%}".format(cn_film1)
        hk_film1 = hk_film / allfilm
        processed_data2 = "{:.2%}".format(hk_film1)
        tw_film1 = tw_film / allfilm
        processed_data3 = "{:.2%}".format(tw_film1)
        result['大陆'] = processed_data
        result['台湾'] = processed_data3
        result['香港'] = processed_data2
        return result

    @staticmethod
    def avg_rate_by_region():
        result = {'cn': {}, 'hk': {}, 'tw': {}}

        # 查询每个地区的年份和平均得分
        cn_data = db.session.query(FilmInfo.year, db.func.avg(FilmInfo.rate)).filter(
            FilmInfo.is_cn == 1).group_by(
            FilmInfo.year).all()
        hk_data = db.session.query(FilmInfo.year, db.func.avg(FilmInfo.rate)).filter(
            FilmInfo.is_hk == 1).group_by(
            FilmInfo.year).all()
        tw_data = db.session.query(FilmInfo.year, db.func.avg(FilmInfo.rate)).filter(
            FilmInfo.is_tw == 1).group_by(
            FilmInfo.year).all()  # 使用like做模糊搜索会出现数据不一致,用辅助列得到结果比region更准确

        # 将查询结果存入结果字典
        for year, avg_rate in cn_data:
            result['cn'][int(year)] = avg_rate
        for year, avg_rate in hk_data:
            result['hk'][int(year)] = avg_rate
        for year, avg_rate in tw_data:
            result['tw'][int(year)] = avg_rate

        return result

    @staticmethod
    def count_by_type():
        result = {}
        # 查询每种类型电影的数量
        data = db.session.query(FilmInfo.type, db.func.count(FilmInfo.id)).group_by(FilmInfo.type).all()
        # data得到的是一个元组，且未经处理
        # 将查询结果存入结果字典
        for film_type, count in data:
            types = film_type.replace("[", "").replace("]", "").split(', ')  # 假设类型数据以逗号分隔,同时把外侧括号去除
            for type in types:
                # 将类型添加到结果字典，并累加数量
                result.setdefault(type, 0)
                # 一个字典方法，用于设置字典中指定键的默认值。该方法的作用是，如果字典中存在指定的键，则返回对应的值；如果字典中不存在指定的键，则将指定的键和默认值添加到字典中，并返回默认值。
                result[type] += count

        return result


    @staticmethod
    def type_rate():
        result = {}
        datas = db.session.query(FilmInfo.type, FilmInfo.rate).all()
        type_list = []
        type_rate_avg = []
        type_rate = 0
        # 获得所有类型
        for data in datas:
            for type in eval(data.type):
                if type not in type_list:
                    type_list.append(type)
        # 求每个类型电影数目和平均人数
        for type in type_list:
            filter_data = FilmInfo.query.filter(FilmInfo.type.contains(type), FilmInfo.rate >= 0).all()
            # 求每个类型的电影数量，同时使用filter过滤无评分数据的电影
            type_num = len(FilmInfo.query.filter(FilmInfo.type.contains(type), FilmInfo.rate >= 0).all())
            # 循环遍历数据，获得总评分人数
            for data in filter_data:
                # 求类型观影总人数
                type_rate += data.rate
            if type_num > 0:
                type_rate_avg.append(type_rate / type_num)
            else:
                type_rate_avg.append(0)
            type_rate = 0  # 为计算下一个类型重置初始值
        result = dict(zip(type_list, type_rate_avg))
        return result


    @staticmethod
    def find_good_directors():
        datas = db.session.query(FilmInfo.director, FilmInfo.rate).all()
        aresult = {}
        director_list = []
        total_movie = 0
        good_movie = 0
        for data in datas:
            for director in eval(data.director):
                if director not in director_list:
                    director_list.append(director)
        for director_name in director_list:
            for data in datas:
                if director_name in data.director:
                    total_movie += 1
                    if data.rate is not None and data.rate >= 8.5:
                        good_movie += 1
            if total_movie > 5:
                aresult[director_name] = good_movie / total_movie
            good_movie = 0
            total_movie = 0
        result = aresult

        # 根据好片占比进行排序并取前十项
        sorted_directors = sorted(result.items(), key=lambda x: x[1], reverse=True)[:10]
        return sorted_directors


    @staticmethod
    def find_good_actors():
        datas = db.session.query(FilmInfo.actor, FilmInfo.rate).all()
        aresult = {}
        actor_list = []
        total_movie = 0
        good_movie = 0
        for data in datas:
            for actor in eval(data.actor):
                if actor not in actor_list:
                    actor_list.append(actor)
        for actor_name in actor_list:
            for data in datas:
                if actor_name in data.actor:
                    total_movie += 1
                    if data.rate is not None and data.rate >= 8.5:
                        good_movie += 1
            if total_movie > 5:
                aresult[actor_name] = good_movie / total_movie
            good_movie = 0
            total_movie = 0
        result = aresult

        # 根据好片占比进行排序并取前十项
        sorted_actors = sorted(result.items(), key=lambda x: x[1], reverse=True)[:10]
        return sorted_actors

    @staticmethod
    def find_best_rate():
        movie = FilmInfo.query.filter(FilmInfo.rating_num > 1000).order_by(FilmInfo.rate.desc()).first()
        result = {}

        result[movie.title] = {
            'rate': movie.rate,
            'time': movie.runtime,
            'rating_num': movie.rating_num
        }
        return result
    @staticmethod
    def find_best_ratenum():
        movie = FilmInfo.query.order_by(FilmInfo.rating_num.desc()).first()
        result = {}
        result[movie.title] = {
            'rate': movie.rate,
            'time': movie.runtime,
            'rating_num': movie.rating_num
        }
        return result
    @staticmethod
    def find_longest_runtime():
        movie = FilmInfo.query.order_by(FilmInfo.runtime.desc()).first()
        result = {}
        result[movie.title] = {
            'rate': movie.rate,
            'time': movie.runtime,
            'rating_num': movie.rating_num
        }
        return result

    @staticmethod
    def find_worst_rate():
        movie = FilmInfo.query.filter(FilmInfo.rating_num > 1000).order_by(FilmInfo.rate.asc()).first()
        result = {}

        result[movie.title] = {
            'rate': movie.rate,
            'time': movie.runtime,
            'rating_num': movie.rating_num
        }
        return result

'''1.不同类型电影平均分 easy ok
2.电影与评分人数关系 mid 
3.好片top10导演 3-6一个问题
4.烂片top10导演 
5.演员
6.演员
'''
