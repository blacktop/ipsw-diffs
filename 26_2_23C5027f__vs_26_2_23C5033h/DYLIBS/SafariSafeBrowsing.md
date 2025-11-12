## SafariSafeBrowsing

> `/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing`

```diff

-623.1.12.10.4
-  __TEXT.__text: 0x60900
-  __TEXT.__auth_stubs: 0xf90
+623.1.13.10.3
+  __TEXT.__text: 0x60b8c
+  __TEXT.__auth_stubs: 0xfa0
   __TEXT.__objc_methlist: 0xb34
-  __TEXT.__gcc_except_tab: 0x6904
+  __TEXT.__gcc_except_tab: 0x6908
   __TEXT.__cstring: 0x19b1
   __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0x1e0e
-  __TEXT.__unwind_info: 0x2be8
+  __TEXT.__oslogstring: 0x1e4b
+  __TEXT.__unwind_info: 0x2bf0
   __TEXT.__objc_classname: 0x217
-  __TEXT.__objc_methname: 0x2579
+  __TEXT.__objc_methname: 0x2580
   __TEXT.__objc_methtype: 0x1206
-  __TEXT.__objc_stubs: 0x18c0
+  __TEXT.__objc_stubs: 0x18e0
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x960
+  __DATA_CONST.__objc_selrefs: 0x968
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x7e0
-  __AUTH_CONST.__const: 0x2828
+  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__const: 0x2858
   __AUTH_CONST.__cfstring: 0x1260
   __AUTH_CONST.__objc_const: 0x18f0
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA.__data: 0x300
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0x3a8
+  __DATA_DIRTY.__bss: 0x3b0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 51754E80-BDBC-37AA-AB94-2BC6DE64018F
-  Functions: 2278
-  Symbols:   6697
-  CStrings:  1091
+  UUID: C2E67F05-325B-3566-9D4C-EA2732A974A8
+  Functions: 2284
+  Symbols:   6712
+  CStrings:  1094
 
Symbols:
+ GCC_except_table167
+ GCC_except_table183
+ GCC_except_table190
+ GCC_except_table211
+ GCC_except_table224
+ GCC_except_table85
+ GCC_except_table89
+ __ZN12SafeBrowsing7Service13checkDeferralEv
+ __ZN12SafeBrowsing7Service13checkDeferralEv.cold.1
+ __ZN7Backend6Google15DatabaseUpdater19cancelAllOperationsEv
+ ____ZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObject_block_invoke.92
+ ___block_descriptor_40_ea8_32c120_ZTSKZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObjectEUlvE__e5_v8?0l
+ ___block_descriptor_56_ea8_32c121_ZTSKZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObjectEUlvE0__e5_v8?0l
+ ___copy_helper_block_ea8_32c121_ZTSKZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObjectEUlvE0_
+ ___destroy_helper_block_ea8_32c121_ZTSKZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObjectEUlvE0_
+ _objc_msgSend$cancel
+ _xpc_activity_should_defer
- GCC_except_table139
- GCC_except_table145
- GCC_except_table149
- GCC_except_table163
- GCC_except_table169
- GCC_except_table177
- GCC_except_table187
- GCC_except_table194
- GCC_except_table208
- GCC_except_table82
- ___block_descriptor_56_ea8_32c120_ZTSKZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObjectEUlvE__e5_v8?0l
- ___destroy_helper_block_ea8_32c120_ZTSKZZN12SafeBrowsing7Service31checkInOrRegisterUpdateActivityEPKcENK3$_0clEPU24objcproto13OS_xpc_object8NSObjectEUlvE_
CStrings:
+ "Database update deferred by DAS"
+ "Failed to defer XPC activity"
+ "cancel"

```
