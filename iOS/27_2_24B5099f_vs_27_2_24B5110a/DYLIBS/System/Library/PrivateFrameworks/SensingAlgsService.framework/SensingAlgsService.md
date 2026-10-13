## SensingAlgsService

> `/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService`

```diff

-72.0.0.0.0
-  __TEXT.__text: 0x20e80
-  __TEXT.__objc_methlist: 0x808
-  __TEXT.__gcc_except_tab: 0xeec
-  __TEXT.__const: 0x1ceb
-  __TEXT.__cstring: 0x42e
-  __TEXT.__oslogstring: 0x182f
+72.1.0.0.0
+  __TEXT.__text: 0x21240
+  __TEXT.__objc_methlist: 0x800
+  __TEXT.__const: 0x1d03
+  __TEXT.__gcc_except_tab: 0xf04
+  __TEXT.__oslogstring: 0x18c3
+  __TEXT.__cstring: 0x440
   __TEXT.__unwind_info: 0xc38
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
+  __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20f8
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0xb78
+  __AUTH_CONST.__cfstring: 0x3c0
+  __AUTH_CONST.__objc_const: 0xb68
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xa4
   __DATA.__data: 0xd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 784
-  Symbols:   1424
-  CStrings:  161
+  Functions: 789
+  Symbols:   1436
+  CStrings:  165
 
Symbols:
+ -[BrailleModeObserver initWithQueue:handler:]
+ -[SASInterfaceTouch initWithStreamSize:platformId:personalityId:queue:streamCallback:]
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table134
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table186
+ GCC_except_table195
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table3
+ GCC_except_table33
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table5
+ _OBJC_IVAR_$_BrailleModeObserver._notifyToken
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ __NSConcreteStackBlock
+ __ZN14SABinaryParser14parseRunHeaderEv
+ __ZN14SABinaryParser19parseLongInjExtDataEPFbPvRK20_SABinaryInjExtPointtjPKhES7_PFbS0_S3_EPFbS0_RK24_SABinaryRunControlPointES7_S7_S9_
+ ___45-[BrailleModeObserver initWithQueue:handler:]_block_invoke
+ ___86-[SASInterfaceTouch initWithStreamSize:platformId:personalityId:queue:streamCallback:]_block_invoke
+ ___block_descriptor_40_ea8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_ea8_32bs_e8_v12?0i8ls32l8
+ ___block_descriptor_40_ea8_32w_e8_v12?0B8lw32l8
+ _dispatch_async
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_alloc
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_retain
+ _objc_retain_x22
- -[BrailleModeObserver brailleEnabled]
- -[BrailleModeObserver init]
- -[BrailleModeObserver setBrailleEnabled:]
- GCC_except_table1
- GCC_except_table123
- GCC_except_table124
- GCC_except_table132
- GCC_except_table185
- GCC_except_table19
- GCC_except_table194
- GCC_except_table2
- GCC_except_table30
- GCC_except_table31
- GCC_except_table4
- GCC_except_table7
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterRemoveObserver
- _OBJC_IVAR_$_BrailleModeObserver._brailleEnabled
- __OBJC_$_PROP_LIST_BrailleModeObserver
- __ZL20NotificationListenerP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary
- __ZN14SABinaryParser19parseLongInjExtDataEPFbPvRK20_SABinaryInjExtPointtjPKhES7_PFbS0_S3_E
- _objc_alloc_init
- _objc_retain_x1
- _objc_retain_x4
CStrings:
+ "24B5105a"
+ "Device supports braille sensing mode, but no queue was provided. Braille mode is disabled"
+ "SensingAlgsService-72.1~21"
+ "[BrailleModeObserver] Failed to register notification: %u"
+ "v12@?0B8"
+ "v12@?0i8"
- "24B5098s"
- "SensingAlgsService-72~1038"
```
