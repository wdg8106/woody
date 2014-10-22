module.exports = function(grunt) {
	//Configure grunt
    grunt.initConfig({
    	pkg : grunt.file.readJSON('package.json'),

    	// 合并文件
        concat: {
            css: {
                // 合并必要的login的css文件
                src: ['src/css/login/*.css'],
                dest: 'dest/css/login.css'
            },
            css2: {
                // 合并必要的index的css文件
                src: ['src/css/index/*.css'],
                dest: 'dest/css/index.css'
            },
            js: {
                // 合并必要的index的js文件
                src: ['src/js/index/*.js'],
                dest: 'dest/js/index.js'
            },
            js2: {
                // 合并必要的base基础js文件
                src: ['src/js/base/*.js'],
                dest: 'dest/js/base.js'
            }
        },

        // 压缩css
        cssmin: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                //美化代码
                beautify: {
                    //中文ascii化，非常有用！防止中文乱码的神配置
                    ascii_only: true
                }
            },
            css: {
                src: 'dest/css/login.css',
                dest: 'dest/css/login.min.css'
            },
            css2: {
                src: 'dest/css/index.css',
                dest: 'dest/css/index.min.css'
            }
        },

        // 压缩js
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n' 
            },
            bulid: {
                src: 'dest/js/index.js',
                dest: 'dest/js/index.min.js'
            },
            bulid2: {
            	src: 'dest/js/base.js',
                dest: 'dest/js/base.min.js'
            }
        },


    	// 压缩图片
        imagemin: {
            dist: {
                files: [{
                    expand: true,
                    cwd: "src/images/",
                    src: ["**/*.{jpg,png,gif,jpeg,ico}"],
                    dest: "dest/images/"
                }]
            }
        },

    	// 连接
	    connect: {
	      options: {
	        port: 9000,

	        hostname: 'localhost',
	        livereload: 35729 
	      },
	      all: {
	        options: {
	          open: true,
	          base: [
	            'src'
	          ]
	        }
	      }
	    },

	    // 监控
	    watch: {
	      livereload: {
	        options: {
	          livereload: '<%= connect.options.livereload %>' 
	        },
	        // 监控你需要监控的文件
	        files: [
	          'src/*.html',
	          'src/js/{,*/}*.js',
	          'src/css/{,*/}*.css',
	          'src/images/{,*/}*.{png,jpg,jpeg,gif,webp,svg}'
	        ]
	      }
	    }
    });

  	// 插件
  	require('time-grunt')(grunt);
  	require('load-grunt-tasks')(grunt);
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-connect');
	grunt.loadNpmTasks('grunt-contrib-imagemin');

    // 创建任务
    grunt.registerTask('default'  , ['connect:all', 'watch']);  // 默认任务，监控并刷新浏览器
    grunt.registerTask('img'      , ['imagemin']);              // 压缩图片，avatar文件夹里的图片压缩会报错
    grunt.registerTask('conFile'  , ['concat']);                // 合并css和js文件
    grunt.registerTask('smallFile', ['cssmin', 'uglify']);      // 压缩css和js文件
};