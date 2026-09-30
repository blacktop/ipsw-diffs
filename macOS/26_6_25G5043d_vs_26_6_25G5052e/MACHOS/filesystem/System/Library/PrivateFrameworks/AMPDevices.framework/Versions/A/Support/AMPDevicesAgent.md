## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent`

```diff

-1.6.6.2.0
-  __TEXT.__text: 0x687164 sha256:5428d32b8afd140134a2c929e016f76e5f90b9a87c15487ba13a8d7fd5713f3b
-  __TEXT.__auth_stubs: 0x58b0 sha256:7b84bd28eb5f03b5f7083788170d9430eb27206bcfd565763653fe44b3333fac
-  __TEXT.__objc_stubs: 0x81e0 sha256:4a496ae0580ca6376c9a25a454080a79e43d97c7d8c92e168ddbb37f6d6abe84
+1.6.6.3.0
+  __TEXT.__text: 0x687164 sha256:da1a2ad27ee299b7a2570830a904cdc2fa08f2d6e9cc536852fbcc8b0b1e5c9b
+  __TEXT.__auth_stubs: 0x58b0 sha256:9460b473d2489318f69f7d4d5627529f6ef8244f2dae7d064911bcaf232a3839
+  __TEXT.__objc_stubs: 0x81e0 sha256:6457099146c6f6130b90f249ce6360c16b033036b31347be3b0d52a39f72b6f6
   __TEXT.__init_offsets: 0x90 sha256:682691dc39cdd19e0e17f34df2a567eba58d07cb1dfb75b24eaa979ecef182a2
   __TEXT.__objc_methlist: 0x1e04 sha256:80a14d4c7b2e58fc9d909a14b3297c983c742312dcfd617954067d340976ad13
   __TEXT.__const: 0x856b0 sha256:423950526da9b6ce4b126acb4ea10ae58a54cd3212be8ed01c0567676434ded3
   __TEXT.__gcc_except_tab: 0x2e514 sha256:784df53cbc7f68f2ded026b2c636a2abcc41639d5b47bc20cdd4865d4c128afa
-  __TEXT.__cstring: 0x60209 sha256:92d1988f18c240b2913bed065634448015916346eb2a90fa6ca8af700cedc8fa
+  __TEXT.__cstring: 0x60209 sha256:ac2b271773f474a96f139cc2e578607f5f3bf528239b49cb62fd5b8b74dd2cda
   __TEXT.__oslogstring: 0x1bfcb sha256:a565218d974741a167e1cbac2de6c28995ca572c6b54628858796ca885d6318a
   __TEXT.__objc_methname: 0x8bd0 sha256:b82f3bd8d3e8ce4009d4bac26d368502e8d55d476d3a0381f510a5e39ba48a96
   __TEXT.__objc_classname: 0x340 sha256:81966a74c8824deb6aecd97c5a66ea15c72f93a86e9b5eb665f3a69305ec9c13
   __TEXT.__objc_methtype: 0x28b6 sha256:c20283acc13837b3155f4b8a0150aac88214273d04536759c59871b9d3efb729
   __TEXT.__unwind_info: 0x12090 sha256:e5cc2048764192b3b0c2833041e147b3fbc96357f5496961a4b246ae46b22a42
-  __TEXT.__eh_frame: 0x1f0 sha256:bc3ec921c8a1481ab6b4318375fc59c0f6c11a1e3a98c31456f8b1f96b75a972
+  __TEXT.__eh_frame: 0x1f0 sha256:32558657226be221fc7d87701c6bfaa6dd0d7dc83d5830fdae236db131539838
   __DATA_CONST.__auth_got: 0x2c70 sha256:a07adae3279bf870f39b51f98f1f927acd7ab08b7292e9498dab6dd63b6ba106
   __DATA_CONST.__got: 0xe98 sha256:b8f46324468958c84b629694b99051bf4ffaa38f3b9a96b6165adcb8f0b4e64c
   __DATA_CONST.__auth_ptr: 0x198 sha256:fe5e3885cde29265cbc687600348baaaa125cfe93c2e43ab422eeb6c5df77d54

   __DATA.__objc_data: 0x550 sha256:dc861ba52f7baf0aec62abc344c58d6907291424cbb2e1d7a1fb063e42c09a52
   __DATA.__data: 0x1798 sha256:de436d30f9edafe135c6689865491c06500af3e697192a110b89aefba51dd194
   __DATA.__common: 0x3af8 sha256:490f55db911b6ed8ffcb4856e7474f036b260c5dd876e8352794b22462df3eda
-  __DATA.__bss: 0x33680 sha256:8ef7aedeed329cdf273eef4dc4243ac782673b8e2f9ea526a0779af680d84ff5
+  __DATA.__bss: 0x33680 sha256:6dbf0a886b52268f756db88fa56453c4f031000a6e538e15a27fd0b3d7a9b083
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EDF2CB9F-0E29-3DF5-8596-8AAF564CEEB7
+  UUID: 7C08123B-1B5F-365A-892D-29A987C12F7F
   Functions: 17771
   Symbols:   1937
   CStrings:  22248
Functions:
~ sub_10047587c : sha256 194cbe2920a56c0345cad82880137a9c3b291398f03f65a4d2613821043eecd7 -> 212832f333ac89a3e0fb11b6a7c86d7112dc0f2607951a711fd940c41acaa434
CStrings:
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10539, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11359, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15704, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15762, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18087, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8485, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "1.6.6.3"
+ "13.6.6.3"
+ "AMPDevicesAgent: 1.6.6.3"
+ "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1303, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/4~CSBFugDEputCnGBRd0Qxq11XMed6LVzopngGa30/Library/Caches/com.apple.xbs/TemporaryDirectory.Wprxxf/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10539, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11359, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15704, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15762, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18087, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8485, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "1.6.6.2"
- "13.6.6.2"
- "AMPDevicesAgent: 1.6.6.2"
- "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1303, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/4~CQ9zugBAZd8KXq2nwHLaFlIgaxJZXEJg5nEkpp4/Library/Caches/com.apple.xbs/TemporaryDirectory.w9ITgk/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"

```
