## SilexWeb

> `/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb`

```diff

-5345.2.0.0.0
-  __TEXT.__text: 0x152d4
+5407.3.0.0.0
+  __TEXT.__text: 0x15504
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x2330
+  __TEXT.__objc_methlist: 0x23a0
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x18ef
+  __TEXT.__cstring: 0x191c
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x780
+  __TEXT.__unwind_info: 0x77c
   __TEXT.__objc_classname: 0x7b8
-  __TEXT.__objc_methname: 0x5e0c
-  __TEXT.__objc_methtype: 0x18d4
-  __TEXT.__objc_stubs: 0x3e00
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x8a8
+  __TEXT.__objc_methname: 0x5ede
+  __TEXT.__objc_methtype: 0x18f8
+  __TEXT.__objc_stubs: 0x3ec0
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7c58
-  __DATA_CONST.__objc_selrefs: 0x11e0
+  __DATA_CONST.__objc_const: 0x7ce8
+  __DATA_CONST.__objc_selrefs: 0x1218
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_classrefs: 0x3b8
+  __DATA_CONST.__objc_classrefs: 0x3c0
   __DATA_CONST.__objc_superrefs: 0x200
-  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x1830
   __AUTH_CONST.__const: 0x7c0
   __AUTH_CONST.__auth_got: 0x250
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x3a4
-  __DATA.__data: 0x14a8
-  __DATA.__bss: 0x40
+  __DATA.__objc_ivar: 0x3b0
+  __DATA.__data: 0x14e8
+  __DATA.__bss: 0x0
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x8

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 783
-  Symbols:   3539
-  CStrings:  1513
+  Functions: 792
+  Symbols:   3568
+  CStrings:  1530
 
Symbols:
+ -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:]
+ -[SWConfiguration networkStatus]
+ -[SWConfiguration setNetworkStatus:]
+ -[SWConfigurationSerializer isNetworkReachableForStatus:]
+ -[SWContainerViewController networkStatus]
+ -[SWContainerViewController reachabilityChanged:]
+ -[SWContainerViewController setNetworkStatus:]
+ -[SWContainerViewController updateReachability]
+ -[SWMutableConfiguration networkStatus]
+ -[SWMutableConfiguration setNetworkStatus:]
+ _OBJC_CLASS_$_NFReachability
+ _OBJC_IVAR_$_SWConfiguration._networkStatus
+ _OBJC_IVAR_$_SWContainerViewController._networkStatus
+ _OBJC_IVAR_$_SWMutableConfiguration.networkStatus
+ __OBJC_$_PROP_LIST_SWActionProvider.94
+ __OBJC_$_PROP_LIST_SWEmbedAction.75
+ _kNFReachabilityChangedNotification
+ _objc_msgSend$currentReachabilityStatus
+ _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:
+ _objc_msgSend$isNetworkReachableForStatus:
+ _objc_msgSend$networkStatus
+ _objc_msgSend$setNetworkStatus:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$updateReachability
- -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:isTransitioning:]
- __OBJC_$_PROP_LIST_SWActionProvider.91
- __OBJC_$_PROP_LIST_SWEmbedAction.72
- _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:isTransitioning:
CStrings:
+ "; networkStatus: %d"
+ "@160@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128B136@140q148B156"
+ "B24@0:8q16"
+ "Tq,N,V_networkStatus"
+ "Tq,N,VnetworkStatus"
+ "_networkStatus"
+ "close"
+ "currentReachabilityStatus"
+ "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:"
+ "isNetworkReachable"
+ "isNetworkReachableForStatus:"
+ "networkStatus"
+ "q"
+ "q16@0:8"
+ "reachabilityChanged:"
+ "setNetworkStatus:"
+ "sharedInstance"
+ "updateReachability"
+ "v24@0:8q16"
- "@152@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128B136@140B148"
- "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:isTransitioning:"

```
