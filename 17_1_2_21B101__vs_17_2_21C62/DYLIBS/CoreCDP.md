## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-359.2.0.0.0
-  __TEXT.__text: 0x30928
+359.4.3.0.0
+  __TEXT.__text: 0x30b4c
   __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x275c
+  __TEXT.__objc_methlist: 0x278c
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0xe28
   __TEXT.__oslogstring: 0x7237
-  __TEXT.__cstring: 0x273b
+  __TEXT.__cstring: 0x27b0
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__unwind_info: 0xd94
   __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x7459
+  __TEXT.__objc_methname: 0x7505
   __TEXT.__objc_methtype: 0x184d
-  __TEXT.__objc_stubs: 0x4220
+  __TEXT.__objc_stubs: 0x42e0
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x1288
+  __DATA_CONST.__const: 0x12a0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x75f8
-  __DATA_CONST.__objc_selrefs: 0x1ac8
+  __DATA_CONST.__objc_const: 0x7638
+  __DATA_CONST.__objc_selrefs: 0x1b00
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__objc_const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x2960
+  __AUTH_CONST.__cfstring: 0x2a20
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0x288
   __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x274
+  __DATA.__objc_ivar: 0x278
   __DATA.__data: 0x790
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1428
-  Symbols:   4771
-  CStrings:  2351
+  Functions: 1432
+  Symbols:   4789
+  CStrings:  2366
 
Symbols:
+ +[CDPUtilities isDemoDevice]
+ -[CDPContext accountType]
+ -[CDPContext setAccountType:]
+ -[CDPContext updateDemoAttributesWithAccount:]
+ _OBJC_IVAR_$_CDPContext._accountType
+ ___block_literal_global.35
+ _kCDPAnalyticsAccountType
+ _kCDPAnalyticsDevicePosture
+ _kCDPAnalyticsSecureChannelProcessApprovalEvent
+ _objc_msgSend$accountType
+ _objc_msgSend$demoAccountForAccount:
+ _objc_msgSend$setAccountType:
+ _objc_msgSend$setDeviceSessionID:
+ _objc_msgSend$setFlowID:
+ _objc_msgSend$updateDemoAttributesWithAccount:
- ___block_literal_global.29
CStrings:
+ "\x02e\x11\x15u#"
+ "Demo"
+ "StoreDemoMode"
+ "T@\"NSString\",C,N,V_accountType"
+ "_accountType"
+ "accountType"
+ "com.apple.corecdp.secureChannelProcess.approval"
+ "com.apple.demo-settings"
+ "demoAccountForAccount:"
+ "devicePosture"
+ "isDemoDevice"
+ "setAccountType:"
+ "setDeviceSessionID:"
+ "setFlowID:"
+ "updateDemoAttributesWithAccount:"
- "\x02e\x11\x15t#"

```
