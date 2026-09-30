## IMDebug

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/IMDebug.framework/IMDebug`

```diff

-4025.400.1.0.0
-  __TEXT.__text: 0x79c4
-  __TEXT.__auth_stubs: 0x6a0
+4025.510.51.1.0
+  __TEXT.__text: 0x7de0
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_stubs: 0x13c0
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x187

   __TEXT.__objc_classname: 0x158
   __TEXT.__objc_methtype: 0x1b3
   __TEXT.__cstring: 0x736
-  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__gcc_except_tab: 0x158
   __TEXT.__oslogstring: 0x24
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x360
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x1a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 51FDACD9-DABC-3A37-B39B-0F23E23E017C
-  Functions: 136
-  Symbols:   609
+  UUID: F7E1B94A-1953-38D1-B59B-BDCD97656C52
+  Functions: 138
+  Symbols:   608
   CStrings:  363
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x24
+ do_extract_currentfile.cold.1
+ main.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x25
- _objc_retain_x8
Functions:
~ -[UIViewController(RecursiveDescription) recursiveDescription] : 96 -> 100
~ -[UIViewController(RecursiveDescription) addDescriptionToString:indentLevel:] : 444 -> 464
~ +[IMDebugDataManager writeDebugData:completion:] : 220 -> 212
~ +[IMDebugDataManager deviceName] : 84 -> 92
~ +[IMDebugDataManager writeDebugDataWithProgress:] : 1816 -> 1916
~ -[IMDebugDownloadReportDataProvider init] : 588 -> 608
~ -[IMDebugDownloadReportDataProvider createDebugDataWithCompletion:] : 232 -> 236
~ -[IMDebugScreenShotDataProvider debugData] : 240 -> 236
~ ___42-[IMDebugScreenShotDataProvider debugData]_block_invoke : 128 -> 140
~ -[IMDebugSyslogDataProvider debugData] : 460 -> 476
~ -[IMDebugUserDefaultsDataProvider debugData] : 132 -> 148
~ -[IMDebugViewControllerHierarchyDataProvider debugData] : 280 -> 284
~ ___55-[IMDebugViewControllerHierarchyDataProvider debugData]_block_invoke : 380 -> 396
~ -[IMDebugViewHierarchyDataProvider debugData] : 280 -> 284
~ ___45-[IMDebugViewHierarchyDataProvider debugData]_block_invoke : 464 -> 492
~ _do_extract_currentfile : 940 -> 936
~ _main : 676 -> 660
~ _unzOpen2 : 960 -> 964
~ _unzlocal_GetCurrentFileInfoInternal : 1096 -> 1116
~ _unzOpenCurrentFile3 : 1460 -> 1444
~ _unzGetLocalExtrafield : 172 -> 176
~ _zipOpen2 : 1428 -> 1416
~ _add_data_in_datablock : 344 -> 324
~ _zipOpenNewFileInZip4 : 2436 -> 2444
~ +[DebugUI isDebugUrl:] : 68 -> 72
~ +[DebugUI showDebugUI] : 456 -> 504
~ +[DebugUI debugViewController] : 84 -> 92
~ +[DebugUI createScreenShotOfPresentedViewController:] : 172 -> 184
~ -[IMDebugViewController viewDidLoad] : 2072 -> 2264
~ -[IMDebugViewController shareData] : 276 -> 296
~ -[IMDebugViewController dismiss] : 72 -> 76
~ -[IMDebugViewController setScreenShotImage:] : 292 -> 312
~ -[IMDebugViewController setScreenShotPreviewImage:] : 20 -> 80
~ -[IMDebugViewController setDataUrl:] : 20 -> 80
~ -[IMDebugViewController setStackView:] : 20 -> 80
~ -[IMDebugViewController setScreenShotImageView:] : 20 -> 80
~ -[IMDebugViewController setActionButton:] : 20 -> 80
~ -[IMDebugViewController setProgressViewContainer:] : 20 -> 80
~ -[IMDebugViewController setProgressView:] : 20 -> 80
~ ___31+[DebugUtil _isInternalInstall]_block_invoke : 88 -> 92
~ +[DebugUtil is17Net] : 120 -> 128
~ +[DebugUtil getIPAddress] : 236 -> 244
~ +[DebugUtil applicationDocumentsDirectory] : 116 -> 128
~ +[DebugUtil allViewControllers] : 208 -> 228
~ +[DebugUtil sharedApplicationIfPossible] : 84 -> 88

```
