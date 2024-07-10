## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Versions/A/WatchListKit`

```diff

-850.0.3.0.0
-  __TEXT.__text: 0x5f9bc
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x5dec
+850.0.1.0.1
+  __TEXT.__text: 0x5ed20
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x5d94
   __TEXT.__const: 0x194
-  __TEXT.__cstring: 0x691f
-  __TEXT.__oslogstring: 0x4848
-  __TEXT.__gcc_except_tab: 0xcbc
-  __TEXT.__unwind_info: 0x1958
-  __TEXT.__objc_classname: 0x117f
-  __TEXT.__objc_methname: 0xdb1a
-  __TEXT.__objc_methtype: 0x18cb
-  __TEXT.__objc_stubs: 0x82e0
+  __TEXT.__cstring: 0x68f5
+  __TEXT.__oslogstring: 0x47a1
+  __TEXT.__gcc_except_tab: 0xc90
+  __TEXT.__unwind_info: 0x1928
+  __TEXT.__objc_classname: 0x116c
+  __TEXT.__objc_methname: 0xd9b6
+  __TEXT.__objc_methtype: 0x1862
+  __TEXT.__objc_stubs: 0x82c0
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__const: 0xa48
-  __DATA_CONST.__objc_classlist: 0x510
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f50
+  __DATA_CONST.__objc_selrefs: 0x2f10
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x2420
-  __AUTH_CONST.__cfstring: 0x9380
-  __AUTH_CONST.__objc_const: 0x110e0
+  __AUTH_CONST.__cfstring: 0x9340
+  __AUTH_CONST.__objc_const: 0x10fe0
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x32a0
-  __DATA.__objc_ivar: 0x978
+  __AUTH.__objc_data: 0x3250
+  __DATA.__objc_ivar: 0x970
   __DATA.__data: 0x620
   __DATA.__bss: 0x4a8
   __DATA.__common: 0x5

   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2428
-  Symbols:   6485
-  CStrings:  1318
+  Functions: 2417
+  Symbols:   6461
+  CStrings:  1316
 
Symbols:
+ -[WLKNetworkRequestOperation setTask:]
+ -[WLKNetworkRequestOperation task]
+ OBJC_IVAR_$_WLKNetworkRequestOperation._task
+ _objc_msgSend$cancel
+ _objc_msgSend$setTask:
+ _objc_msgSend$task
- +[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:error:]
- +[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:error:].cold.1
- +[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:activity:completion:]
- -[WLKMetricsActivity .cxx_destruct]
- -[WLKMetricsActivity activity]
- -[WLKMetricsActivity initWithLabel:]
- -[WLKMetricsActivity label]
- -[WLKNetworkRequestOperation initWithURLRequest:options:activity:]
- -[WLKNetworkRequestOperation nwactivity]
- -[WLKNetworkRequestOperation setNwactivity:]
- OBJC_IVAR_$_WLKMetricsActivity._activity
- OBJC_IVAR_$_WLKMetricsActivity._label
- OBJC_IVAR_$_WLKNetworkRequestOperation._nwactivity
- _OBJC_CLASS_$_WLKMetricsActivity
- _OBJC_METACLASS_$_WLKMetricsActivity
- _WLKIsNLSBubbleTipEnabledInCache
- __OBJC_$_INSTANCE_METHODS_WLKMetricsActivity
- __OBJC_$_INSTANCE_VARIABLES_WLKMetricsActivity
- __OBJC_$_PROP_LIST_WLKMetricsActivity
- __OBJC_CLASS_RO_$_WLKMetricsActivity
- __OBJC_METACLASS_RO_$_WLKMetricsActivity
- ___107+[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:activity:completion:]_block_invoke
- ___WLKIsNLSBubbleTipEnabledInCache_block_invoke
- _nw_activity_activate
- _nw_activity_create
- _objc_msgSend$_prepareEncoder:account:sessionConfiguration:options:error:
- _objc_msgSend$activity
- _objc_msgSend$dataTaskPromiseWithRequest:activity:
- _objc_msgSend$invalidateAndCancel
CStrings:
- "FeatureEnablementAdditionalFlags"
- "pretoria"

```
