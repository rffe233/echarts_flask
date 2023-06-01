import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import * as echarts from 'echarts';
import {catchError, Observable, of, tap} from "rxjs"
import { filmService } from './film.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent  implements OnInit {
  filmData: any;options: any;options1:any;options2:any;
  options3:any;options4:any;options5:any;filmnumber:any;
  options6:any;options7:any;options8:any;options9:any;
  movieName2:any;rate2:any;ratenum2:any;time2:any;
  movieName3:any;rate3:any;ratenum3:any;time3:any;
  movieName4:any;rate4:any;ratenum4:any;
  time4:any;movieName1:any;rate1:any;ratenum1:any;
  time1:any;options10:any;



  constructor(private filmService: filmService) {
  }

  ngOnInit() {
    this.filmService.getFilmCountByYear().subscribe(data => {
      this.filmData = data;
      const years = Object.keys(data);
      const counts = Object.values(data);
      this.options = {
        xAxis: {
          type: 'category',
          data: years
        },
        yAxis: {
          type: 'value'
        },
        series: [
      // {
        //   data: counts,
        //   type: 'bar',
        // },
       {
          data: counts,
          type: 'line',
        }],
        tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
          trigger: 'axis',
          backgroundColor: 'rgba(32, 33, 36,.7)',
          borderColor: 'rgba(32, 33, 36,0.20)',
          borderWidth: 1,
          textStyle: { // 文字提示样式
            color: '#fff',
            fontSize: '12'
          },
        }
      };
    });
    this.filmService.getratenum_year().subscribe(data => {
      this.filmData = data;
      const years = Object.keys(data);
      const counts = Object.values(data);
      this.options9 = {
        xAxis: {
          type: 'category',
          data: years
        },
        yAxis: {
          type: 'value'
        },
        series: [
          // {
          //   data: counts,
          //   type: 'bar',
          // },
          {
            data: counts,
            type: 'line',
          }],
        tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
          trigger: 'axis',
          backgroundColor: 'rgba(32, 33, 36,.7)',
          borderColor: 'rgba(32, 33, 36,0.20)',
          borderWidth: 1,
          textStyle: { // 文字提示样式
            color: '#fff',
            fontSize: '12'
          },
        }
      };
    });
    this.filmService.getFilmCountByType().subscribe(data => {
      this.filmData = data;
      const types = Object.keys(data);
      const counts = Object.values(data);
      this.options1 = {
        xAxis: {
          type: 'category',
          data: types,
          axisTick: {
            alignWithLabel: true
          },
         // axisLabel: {
         //    interval:0
         // }
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: counts,
          type: 'bar',
        }],
        tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
          trigger: 'axis',
          backgroundColor: 'rgba(32, 33, 36,.7)',
          borderColor: 'rgba(32, 33, 36,0.20)',
          borderWidth: 1,
          textStyle: { // 文字提示样式
            color: '#fff',
            fontSize: '12'
          },
          // axisPointer: { // 坐标轴虚线
          //   type: 'cross',
          //   label: {
          //     backgroundColor: '#6a7985'
          //   }
          // },
         }
        };
    });

    this.filmService.getavg_rate_by_region().subscribe(data => {
      this.filmData = data;
      const cnData = data["cn"];
      const hkData = data["hk"];
      const twData = data["tw"];

      const years = Object.keys(cnData);
      const movieData = years.map(year => ({
        year: year,
        cn: cnData[year],
        hk: hkData[year],
        tw: twData[year]
      }));

      this.options10 = {
        xAxis: {
          type: 'category',
          data: years,
          axisTick: {
            alignWithLabel: true
          },
        },
        yAxis: {},
        series: [
          {
            type: 'bar',
            name: 'cn',
            data: movieData.map(item => item.cn)
          },
          {
            type: 'bar',
            name: 'hk',
            data: movieData.map(item => item.hk)
          },
          {
            type: 'bar',
            name: 'tw',
            data: movieData.map(item => item.tw)
          }
        ],
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['cn', 'hk', 'tw'],
          selectedMode: 'multiple',
          selected: { // 设置所有图例项为选中状态
            'cn': true,
            'hk': true,
            'tw': true
          },
          textStyle: {
            color: 'yellow' // 设置字体颜色
          }
        },
        dataZoom: [
          {
            type: 'slider', // 滑动条型数据视图
            xAxisIndex: 0, // 对应 x 轴的索引，默认为 0
            start: 0, // 默认数据视图范围的起始位置为 0%
            end: 10 // 默认数据视图范围的结束位置为 10%
          }]
      };
    });

    // this.filmService.getavg_rate_by_region().subscribe(data => {
    //   this.filmData = data;
    //   const cn_data = Object.keys(data)[0];
    //   const year = Object.keys(cn_data);
    //   const tw_data = Object.keys(data)[2];
    //   const hk_data = Object.keys(data)[1];
    //   const year1 = Object.keys(tw_data);
    //   const year2 = Object.keys(hk_data);
    //   const cn_moviedata = Object.values(year)
    //   const hk_moviedata = Object.values(year2)
    //   const tw_moviedata = Object.values(year1)
    //
    //
    //   this.options10 = {
    //     xAxis: {
    //       type: 'category',
    //       data: year,
    //       axisTick: {
    //         alignWithLabel: true
    //       },
    //       // axisLabel: {
    //       //    interval:0
    //       // }
    //     },
    //     yAxis: {
    //     },
    //     series: [{
    //       type: 'bar',
    //       name: 'cn',
    //       data: cn_moviedata
    //     },
    //       {
    //         type: 'bar',
    //         name: 'hk',
    //         data: hk_moviedata
    //       },
    //       {
    //         type: 'bar',
    //         name: 'tw',
    //         data: tw_moviedata
    //       }
    //     ],
    //     tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
    //       trigger: 'axis',
    //       backgroundColor: 'rgba(32, 33, 36,.7)',
    //       borderColor: 'rgba(32, 33, 36,0.20)',
    //       borderWidth: 1,
    //       textStyle: { // 文字提示样式
    //         color: '#fff',
    //         fontSize: '12'
    //       },
    //       // axisPointer: { // 坐标轴虚线
    //       //   type: 'cross',
    //       //   label: {
    //       //     backgroundColor: '#6a7985'
    //       //   }
    //       // },
    //     }
    //   };
    // });
    this.filmService.getFilmTypeByYear().subscribe(data => {
      this.filmData = data;
      const types = Object.keys(data);
      const rates = Object.values(data);
      this.options8 = {
        xAxis: {
          type: 'category',
          data: types,
          axisTick: {
            alignWithLabel: true
          },
          // axisLabel: {
          //    interval:0
          // }
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: rates,
          type: 'lines',
        }],
        tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
          trigger: 'axis',
          backgroundColor: 'rgba(32, 33, 36,.7)',
          borderColor: 'rgba(32, 33, 36,0.20)',
          borderWidth: 1,
          textStyle: { // 文字提示样式
            color: '#fff',
            fontSize: '12'
          },
          // axisPointer: { // 坐标轴虚线
          //   type: 'cross',
          //   label: {
          //     backgroundColor: '#6a7985'
          //   }
          // },
        }
      };
    });
    this.filmService.getFilmRate().subscribe(data => {
      this.filmData = data;
      const names = Object.keys(data);
      const counts = Object.values(data);

      const dataPoints = names.map((name, index) => {
        return {
          name: name,
          value: counts[index],

        };
      });

      this.options2 = {
        series: [
          {
            type: 'pie',
            data: dataPoints,
            label: {
              show: true, // 显示标签
              formatter: '{b}', // 设置标签格式为显示名称（name）
              position: 'inside' // 标签位置为外部
            }
          }
        ],
        tooltip: {
          trigger: 'item', // 设置触发类型为 'item'
          backgroundColor: 'rgba(32, 33, 36, .7)',
          borderColor: 'rgba(32, 33, 36, 0.2)',
          borderWidth: 1,
          textStyle: {
            color: '#fff',
            fontSize: '12'
          },
          formatter: '{b}: {c}' // 设置显示的文本格式，{b} 表示名称，{c} 表示值
        }
      };
    });
    this.filmService.getFilmTime().subscribe(data => {
      this.filmData = data;
      const names = Object.keys(data);
      const counts = Object.values(data);

      const dataPoints = names.map((name, index) => {
        return {
          name: name,
          value: counts[index],

        };
      });

      this.options3 = {
        series: [
          {
            type: 'pie',
            data: dataPoints,
            label: {
              show: true, // 显示标签
              formatter: '{b}', // 设置标签格式为显示名称（name）
              position: 'inside' // 标签位置为外部
            }
          }
        ],
        tooltip: {
          trigger: 'item', // 设置触发类型为 'item'
          backgroundColor: 'rgba(32, 33, 36, .7)',
          borderColor: 'rgba(32, 33, 36, 0.2)',
          borderWidth: 1,
          textStyle: {
            color: '#fff',
            fontSize: '12'
          },
          formatter: '{b}: {c}' // 设置显示的文本格式，{b} 表示名称，{c} 表示值
        }
      };
    });
    this.filmService.getFilmRegion().subscribe(data => {
      this.filmData = data;
      const names = Object.keys(data);
      const counts = Object.values(data);

      const dataPoints = names.map((name, index) => {
        return {
          name: name,
          value: counts[index],

        };
      });

      this.options4 = {
        series: [
          {
            type: 'pie',
            data: dataPoints,
            label: {
              show: true, // 显示标签
              formatter: '{b}', // 设置标签格式为显示名称（name）
              position: 'inside' // 标签位置为外部
            }
          }
        ],
        tooltip: {
          trigger: 'item', // 设置触发类型为 'item'
          backgroundColor: 'rgba(32, 33, 36, .7)',
          borderColor: 'rgba(32, 33, 36, 0.2)',
          borderWidth: 1,
          textStyle: {
            color: '#fff',
            fontSize: '12'
          },
          formatter: '{b}: {c}' // 设置显示的文本格式，{b} 表示名称，{c} 表示值
        }
      };
    });

    this.filmService.getFilmNumber().subscribe(filmnumber =>
      this.filmnumber=filmnumber)
    this.filmService.getgood_director().subscribe(data => {
      this.filmData = data;
      const names = data.map((item: any[]) => item[0]);;
      const counts = data.map((item: any[]) => item[1]); ;
      this.options6 = {
        xAxis: {
          type: 'category',
          data: names,
          axisLabel: {
               interval:0
            }
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: counts,
            type: 'bar',
          }],
        tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
          trigger: 'axis',
          backgroundColor: 'rgba(32, 33, 36,.7)',
          borderColor: 'rgba(32, 33, 36,0.20)',
          borderWidth: 1,
          textStyle: { // 文字提示样式
            color: '#fff',
            fontSize: '12'
          },
        }
      };
    });
    this.filmService.getgood_actor().subscribe(data => {
      this.filmData = data;
      const names = data.map((item: any[]) => item[0]);
      const counts = data.map((item: any[]) => item[1]);
      this.options7 = {
        xAxis: {
          type: 'category',
          data: names
        },
        yAxis: {
          type: 'value'
        },
        series: [
          // {
          //   data: counts,
          //   type: 'bar',
          // },
          {
            data: counts,
            type: 'bar',
          }],
        tooltip: { // 鼠标悬浮提示框显示 X和Y 轴数据
          trigger: 'axis',
          backgroundColor: 'rgba(32, 33, 36,.7)',
          borderColor: 'rgba(32, 33, 36,0.20)',
          borderWidth: 1,
          textStyle: { // 文字提示样式
            color: '#fff',
            fontSize: '12'
          },
        }
      };
    });
    this.filmService.getbest_movie().subscribe(data => {
      this.filmData = data;
      const movieName1 = Object.keys(data)[0];
      const rate1 = data[movieName1]['rate'];
      const rating_num1 = data[movieName1]['rating_num'];
      const time1 = data[movieName1]['time'];
      this.movieName1 = movieName1;
      this.rate1= rate1;
      this.ratenum1 = rating_num1;
      this.time1 = time1
    })
    this.filmService.getbest_rateum().subscribe(data => {
      this.filmData = data;
      const movieName2 = Object.keys(data)[0];
      const rate2 = data[movieName2]['rate'];
      const rating_num2 = data[movieName2]['rating_num'];
      const time2 = data[movieName2]['time'];
      this.movieName2 = movieName2;
      this.rate2= rate2;
      this.ratenum2 = rating_num2;
      this.time2 = time2
    })
    this.filmService.getlongest_movie().subscribe(data => {
      this.filmData = data;
      const movieName3 = Object.keys(data)[0];
      const rate3 = data[movieName3]['rate'];
      const rating_num3 = data[movieName3]['rating_num'];
      const time3 = data[movieName3]['time'];
      this.movieName3 = movieName3;
      this.rate3= rate3;
      this.ratenum3 = rating_num3;
      this.time3 = time3
    })
    this.filmService.getworst_movie().subscribe(data => {
      this.filmData = data;
      const movieName4 = Object.keys(data)[0];
      const rate4 = data[movieName4]['rate'];
      const rating_num4 = data[movieName4]['rating_num'];
      const time4 = data[movieName4]['time'];
      this.rate4= rate4;
      this.ratenum4 = rating_num4;
      this.time4 = time4
    })

  }
}



