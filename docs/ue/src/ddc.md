# [派生数据缓存](https://openhutb.github.io/engine_doc/zh-CN/ProductionPipelines/DerivedDataCache/index.html)

派生数据缓存 (Derived Data Cache, DDC) 存储了一个资源的版本，这个版本是引擎在目标平台上所用的格式。与此相对的是艺术家所创建的原始格式的资源，那些资源被导入到引擎编辑器中存储成了`.uasset`文件。

存储在 DDC 中的内容可以随时丢弃，因为他们可以随时由 `.uasset` 文件重新生成。

在外部存储派生格式是为了可以随时添加或更改引擎所用的格式，而不需要修改原始资源文件（指`.uasset`文件）。



## 参考

* [观察DDC（DerivedDataCache）](https://blog.csdn.net/u013412391/article/details/105546408/)