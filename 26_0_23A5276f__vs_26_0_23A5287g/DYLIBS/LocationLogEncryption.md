## LocationLogEncryption

> `/System/Library/PrivateFrameworks/LocationLogEncryption.framework/LocationLogEncryption`

```diff

-3056.0.0.0.0
-  __TEXT.__text: 0x19dc
-  __TEXT.__auth_stubs: 0x350
+3056.0.6.0.2
+  __TEXT.__text: 0x1dc4
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x94
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x224
-  __TEXT.__oslogstring: 0x39f
-  __TEXT.__cstring: 0x183
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__oslogstring: 0x442
+  __TEXT.__cstring: 0x1dd
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x2a3

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x100
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x2004
   __DATA.__objc_ivar: 0x8
-  __DATA.__bss: 0x58
+  __DATA.__data: 0x18
+  __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE0F185A-95FF-3274-8B85-C6D22725E8BB
-  Functions: 20
-  Symbols:   75
-  CStrings:  84
+  UUID: 70F06097-26D3-3365-A8E4-C362EB32F4C7
+  Functions: 21
+  Symbols:   80
+  CStrings:  90
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFRelease
+ _MGCopyAnswer
CStrings:
+ "InternalBuild"
+ "Key created successfully: %{public}s"
+ "Location log encryption is disabled on customer builds, locations will be redacted"
+ "LocationLogEncryptionLoadOrCreateKey"
+ "LocationLogEncryptionLoadOrCreateKey() must be called only on internal installs"
+ "LocationLogEncryptionSetKeyActive"
+ "selectEncryptionKey"
- "key created successfully: %{public}s"
- "toggleKeyIndex"

```
