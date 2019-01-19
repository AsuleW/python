 ### step 1:
  `autoscan ` 
  `生成的文件有:autoscan.log  configure.scan`

 ### step 2:
 `
  修改configure.scan 为configure.ac;
  修改configure.ac内容
  修改
  AC_INIT([FULL-PACKAGE-NAME], [VERSION], [BUG-REPORT-ADDRESS])
  为
  AC_INIT(main, 1.0, asule.w@hotmai.com)
  ps:main：是可执行文件名 1.0为版本号 asule.w@hotmail.com:邮件名`

  `另外添加 AM_INIT_AUTOMAKE(main, 1.0) 一定要添加`
`
 ###  step 3:
  `autoheader     ----> config.h.in`

 ###  step 4:
  `aclocal        ----> 生成aclocal.m4 必须要有 AM_INIT_AUTOMAKE宏`

 ### step 5:
 ` 写Makefile.am文件 
  Makefile.am文件内容`
  
  `AUTOMAKE_OPTIONS=foreign
  bin_PROGRAMS=main
  main_SOURCES=main.cpp`

 ### step 6:
  `automake --add-missing      ------->生成 Makefile.in`

 ### step 7:
  `autoconf                    ------->生成 configure`

 ### step 8: 
  `./configure                ------->生成Makefile`

 ### step 9: 
  `make `

 ### step 10: 
  `运行 main`

 ### step 11:
  `make dist 打包`

    
