## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0xda84
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x11a8
+54.1.2.0.0
+  __TEXT.__text: 0xde94
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x11e0
   __TEXT.__const: 0x80
-  __TEXT.__oslogstring: 0x94d
-  __TEXT.__cstring: 0xc06
-  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__oslogstring: 0xa47
+  __TEXT.__cstring: 0xc95
+  __TEXT.__gcc_except_tab: 0x168
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4a0
-  __TEXT.__objc_classname: 0x25f
-  __TEXT.__objc_methname: 0x2f8e
-  __TEXT.__objc_methtype: 0x777
-  __TEXT.__objc_stubs: 0x23a0
+  __TEXT.__unwind_info: 0x4b4
+  __TEXT.__objc_classname: 0x276
+  __TEXT.__objc_methname: 0x2fa8
+  __TEXT.__objc_methtype: 0x796
+  __TEXT.__objc_stubs: 0x23c0
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x858
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2478
-  __DATA_CONST.__objc_selrefs: 0xd70
-  __AUTH_CONST.__objc_const: 0x40
-  __AUTH_CONST.__cfstring: 0xaa0
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x458
+  __DATA_CONST.__objc_const: 0x24a0
+  __DATA_CONST.__objc_selrefs: 0xd78
+  __AUTH_CONST.__objc_const: 0xd0
+  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x470
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0x8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x140
+  __DATA.__objc_classrefs: 0x148
   __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0x130
+  __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x2a8
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__const: 0x140
   __DATA_DIRTY.__objc_const: 0xa68
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0FC22025-1A56-35A6-AE82-6CE90B91CB02
-  Functions: 487
-  Symbols:   1936
-  CStrings:  998
+  UUID: 58FA9A2B-24C1-39F7-AD00-0F194EC7DA04
+  Functions: 496
+  Symbols:   1969
+  CStrings:  1015
 
Symbols:
+ +[AAFKeybagLockAssertion lockWithError:]
+ +[AAFKeybagLockAssertion lockWithError:].cold.1
+ +[AAFKeybagLockAssertion lock]
+ -[AAFAnalyticsEvent setObject:forKeyedSubscript:].cold.1
+ -[AAFAnalyticsEvent setObject:forKeyedSubscript:].cold.2
+ -[AAFKeybagLockAssertion unlock]
+ _MobileKeyBagLibrary.frameworkLibrary
+ _OBJC_CLASS_$_AAFKeybagLockAssertion
+ _OBJC_IVAR_$_AAFKeybagLockAssertion._assertionRef
+ _OBJC_METACLASS_$_AAFKeybagLockAssertion
+ __OBJC_$_CLASS_METHODS_AAFKeybagLockAssertion
+ __OBJC_$_INSTANCE_METHODS_AAFKeybagLockAssertion
+ __OBJC_$_INSTANCE_VARIABLES_AAFKeybagLockAssertion
+ __OBJC_CLASS_RO_$_AAFKeybagLockAssertion
+ __OBJC_METACLASS_RO_$_AAFKeybagLockAssertion
+ _dlopen
+ _initMKBDeviceLockAssertion
+ _initMKBDeviceLockAssertion.cold.1
+ _initMKBDeviceLockAssertion.cold.2
+ _objc_msgSend$lockWithError:
+ _objc_sync_enter
+ _objc_sync_exit
+ _softLinkMKBDeviceLockAssertion
CStrings:
+ "\"AAFAnalyticsEvent gets a nil key. Please check if the key is constructed properly.\""
+ "\"AAFAnalyticsEvent gets a nil object. Please check if the payload is constructed properly.\""
+ "/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
+ "@24@0:8^@16"
+ "AAFKeybagLockAssertion"
+ "Failed to take device lock assertion: %@"
+ "MKBAssertionKey"
+ "MKBAssertionTimeout"
+ "MKBDeviceLockAssertion"
+ "Releasing device lock assertion"
+ "RemoteProfile"
+ "^{__MKBAssertion=}"
+ "_assertionRef"
+ "lockWithError:"

```
