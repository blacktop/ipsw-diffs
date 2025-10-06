## SoftwareUpdateCoreSupport

> `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport`

```diff

-1856.80.3.0.1
-  __TEXT.__text: 0x323e8
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x3008
-  __TEXT.__cstring: 0x784e
+1856.100.79.0.3
+  __TEXT.__text: 0x32644
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x3020
+  __TEXT.__cstring: 0x78cb
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x4f8
-  __TEXT.__oslogstring: 0x4f54
-  __TEXT.__unwind_info: 0xa84
+  __TEXT.__oslogstring: 0x5055
+  __TEXT.__unwind_info: 0xa88
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0xaa43
+  __TEXT.__objc_methname: 0xaa7d
   __TEXT.__objc_methtype: 0xce7
-  __TEXT.__objc_stubs: 0x6cc0
+  __TEXT.__objc_stubs: 0x6d20
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x1190
+  __DATA_CONST.__const: 0x11c0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3a00
-  __DATA_CONST.__objc_selrefs: 0x2148
-  __AUTH_CONST.__cfstring: 0x78a0
-  __AUTH_CONST.__objc_const: 0x0
+  __DATA_CONST.__objc_const: 0x39b8
+  __DATA_CONST.__objc_selrefs: 0x2160
+  __DATA_CONST.__objc_classrefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __AUTH_CONST.__cfstring: 0x7980
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x338
-  __DATA.__objc_classrefs: 0x1e0
-  __DATA.__objc_superrefs: 0xc0
+  __AUTH_CONST.__auth_got: 0x350
   __DATA.__objc_ivar: 0x40c
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B660F18E-49DD-3D8E-895B-39B830D5B931
-  Functions: 1192
-  Symbols:   4177
-  CStrings:  4011
+  UUID: 5F965926-E2FC-337E-B786-8B7D6EEFE508
+  Functions: 1193
+  Symbols:   4193
+  CStrings:  4033
 
Symbols:
+ +[SUCoreEvent isSharediPad]
+ _OBJC_CLASS_$_UMUserManager
+ __OBJC_$_CLASS_METHODS_SUCoreEvent
+ _kSUCoreControllerClientNameKey
+ _kSUCoreControllerDownloadOverCellularKey
+ _kSUCoreControllerEventOTAStartedDownloading
+ _kSUCoreControllerMandatoryUpdateEligibleKey
+ _kSUCoreControllerMandatoryUpdateOptionalKey
+ _kSUCoreControllerNetworkTypeKey
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$isSharediPad
+ _objc_msgSend$sharedManager
+ _objc_opt_respondsToSelector
CStrings:
+ "T@\"NSString\",?,R,C"
+ "[EVENT_REPORTER] Detected shared iPad"
+ "[EVENT_REPORTER] UMUserManager class does not exist."
+ "[EVENT_REPORTER] UMUserManager class does not respond to selector 'sharedManager'"
+ "[EVENT_REPORTER] UMUserManager instance does not respond to selector 'isSharedIPad'"
+ "clientName"
+ "downloadOverCellular"
+ "isSharedIPad"
+ "isSharediPad"
+ "mandatoryUpdateEligible"
+ "mandatoryUpdateOptional"
+ "networkType"
+ "otaStartedDownloading"
+ "sharedManager"
+ "sharediPad"

```
