from flask import Blueprint, jsonify, request
from models.films import FilmInfo
import logging  # 使用日志记录相关信息

logging.basicConfig(filename='films_api.log', level=logging.DEBUG)
films_bp = Blueprint('films', __name__)


@films_bp.route('/', methods=['GET'])
def get_films():
    # 返回所有的电影信息
    try:  # 在所有的路由中，都要进行错误处理
        films = FilmInfo.query.all()
        results = []
        for film in films:
            results.append(film.to_dict())
        logging.info('All films were successfully retrieved from the database.')  # 用logging模块记录日志
        return jsonify(results)
    except Exception as e:
        logging.error('Error occurred while retrieving films from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})  # 报错  "error": "'list' object has no attribute 'to_dict'"


# 计算每年电影数量
@films_bp.route('/count_by_year', methods=['GET'])
def count_by_year():
    try:
        result = FilmInfo.count_by_year()
        logging.info('获得各年份电影数量序列')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 计算每年电影评分人数，其中为0的不算入分母
@films_bp.route('/ratenum_by_year', methods=['GET'])
def ratenum_by_year():
    try:
        result = FilmInfo.ratenum_by_year()
        logging.info('获得各年份电影评分人数序列')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得年电影平均评分
@films_bp.route('/rate_by_year', methods=['GET'])
def rate_by_year():
    try:
        result = FilmInfo.ratem_by_year()
        logging.info('获得各年份电影平均分序列')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得影片中好片、普通、烂片占比
@films_bp.route('/film_rate', methods=['GET'])
def get_film_rate():
    try:
        result = FilmInfo.get_film_rate()
        logging.info('获得各年份电影质量情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得影片时间分布情况
@films_bp.route('/film_time', methods=['GET'])
def get_film_time():
    try:
        result = FilmInfo.get_film_time()
        logging.info('获得影片时间分布情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得影片地区分布情况
@films_bp.route('/film_region', methods=['GET'])
def get_film_region():
    try:
        result = FilmInfo.get_film_region()
        logging.info('获得影片地区分布情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得电影总数量
@films_bp.route('/film_number', methods=['GET'])
def get_film_num():
    try:
        result = FilmInfo.get_film_num()
        logging.info('获得电影总数量')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得地区电影评分按时间分布情况
@films_bp.route('/avg_rate_by_region', methods=['GET'])
def avg_rate_by_region():
    try:
        result = FilmInfo.avg_rate_by_region()
        logging.info('获得地区电影评分按时间分布情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得电影数量按种类分布情况
@films_bp.route('/count_by_type', methods=['GET'])
def count_by_type():
    try:
        result = FilmInfo.count_by_type()
        logging.info('获得电影数量按种类分布情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得种类与评分人数情况
@films_bp.route('/type_ratenum', methods=['GET'])
def type_ratenum():
    try:
        result = FilmInfo.type_ratenum()
        logging.info('获得种类与评分人数情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 获得种类与评分情况
@films_bp.route('/type_rate', methods=['GET'])
def type_rate():
    try:
        result = FilmInfo.type_rate()
        logging.info('获得种类与评分情况')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# @films_bp.route('/relation', methods=['GET'])
# def film_relation_ratenum():
#     try:
#         result = FilmInfo.film_relation_ratenum()  # 直接调用FilmInfo类中构建的静态方法type_ratenum
#         logging.info('不同类型电影数量')
#         return jsonify(result)
#     except Exception as e:
#         logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
#         return jsonify({"error": str(e)})

# 最佳十个导演
@films_bp.route('/gooddirector', methods=['GET'])
def find_good_dictor():
    try:
        result = FilmInfo.find_good_directors()
        logging.info('最佳导演')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# @films_bp.route('/baddirector', methods=['GET'])
# def find_bad_dictor():
#     try:
#         result = FilmInfo.find_bad_directors()  # 直接调用FilmInfo类中构建的静态方法type_ratenum
#         logging.info('不同类型电影数量')
#         return jsonify(result)
#     except Exception as e:
#         logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
#         return jsonify({"error": str(e)})

# 最佳演员
@films_bp.route('/goodactor', methods=['GET'])
def find_good_actors():
    try:
        result = FilmInfo.find_good_actors()
        logging.info('最佳演员')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


#
# @films_bp.route('/badactor', methods=['GET'])
# def find_bad_actors():
#     try:
#         result = FilmInfo.find_bad_actors()  # 直接调用FilmInfo类中构建的静态方法type_ratenum
#         logging.info('不同类型电影数量')
#         return jsonify(result)
#     except Exception as e:
#         logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
#         return jsonify({"error": str(e)})

# 最佳评分电影
@films_bp.route('/bestrate', methods=['GET'])
def find_best_rate():
    try:
        result = FilmInfo.find_best_rate()
        logging.info('最佳评分电影')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 最差评分电影
@films_bp.route('/worstrate', methods=['GET'])
def find_worst_rate():
    try:
        result = FilmInfo.find_worst_rate()
        logging.info('最差评分电影')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 最多评分人数
@films_bp.route('/bestratenum', methods=['GET'])
def find_best_ratenum():
    try:
        result = FilmInfo.find_best_ratenum()
        logging.info('最多评分人数')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


# 最长时间电影
@films_bp.route('/longestruntime', methods=['GET'])
def find_longest_runtime():
    try:
        result = FilmInfo.find_longest_runtime()
        logging.info('最长时间电影')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})
