# ipython

可以先在 ipython 进行编程测试，再复制代码到编辑器

```shell
In [1]: line = "MySQL slave binlog position: master host '10.173.33.35', filename 'mysql-bin.000002', position '524993060'"

In [2]: line.split("'")
Out[2]:
['MySQL slave binlog position: master host ',
 '10.173.33.35',
 ', filename ',
 'mysql-bin.000002',
 ', position ',
 '524993060',
 '']

In [3]: host = line.split("'")[1]

In [4]: host
Out[4]: '10.173.33.35'

In [5]: filename = line.split("'")[3]

In [6]: filename
Out[6]: 'mysql-bin.000002'

In [7]: position = line.split("'")[5]

In [8]: position
Out[8]: '524993060'

In [9]: position = int(position)

In [10]: print(host, filename, position)
10.173.33.35 mysql-bin.000002 524993060
```

```shell
In [1]: import os

In [3]: ?os.path.is*
os.path.isabs
os.path.isdir
os.path.isfile
os.path.islink
os.path.ismount

In [5]: os.path.isfile?
Signature: os.path.isfile(path)
Docstring: Test whether a path is a regular file
File:      /usr/local/Caskroom/miniconda/base/envs/ops/lib/python3.9/genericpath.py
Type:      function

```

```shell
In [21]: %lsmagic
Out[21]:
Available line magics:
%alias  %alias_magic  %autoawait  %autocall  %autoindent  %automagic  %bookmark  %cat  %cd  %clear  %colors  %conda  %config  %cp  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %man  %matplotlib  %mkdir  %more  %mv  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile

Automagic is ON, % prefix IS NOT needed for line magics.
```
