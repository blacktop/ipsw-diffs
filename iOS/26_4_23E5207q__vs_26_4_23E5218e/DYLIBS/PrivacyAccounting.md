## PrivacyAccounting

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting`

```diff

-147.0.0.0.0
-  __TEXT.__text: 0x1f91c
+148.0.0.0.0
+  __TEXT.__text: 0x1f8c0
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x210c
+  __TEXT.__objc_methlist: 0x2114
   __TEXT.__const: 0x698
   __TEXT.__cstring: 0x10bc
   __TEXT.__oslogstring: 0x93f

   __TEXT.__unwind_info: 0xb10
   __TEXT.__eh_frame: 0x228
   __TEXT.__objc_classname: 0x7f9
-  __TEXT.__objc_methname: 0x38fa
-  __TEXT.__objc_methtype: 0xd08
+  __TEXT.__objc_methname: 0x391a
+  __TEXT.__objc_methtype: 0xd28
   __TEXT.__objc_stubs: 0x2aa0
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x8b0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe08
+  __DATA_CONST.__objc_selrefs: 0xe10
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x140
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x4610
+  __AUTH_CONST.__objc_const: 0x4640
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x980
   __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x224
+  __DATA.__objc_ivar: 0x228
   __DATA.__data: 0xa60
   __DATA.__bss: 0x5c8
   __DATA_DIRTY.__objc_data: 0x6b0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 818BC284-50D5-3729-9C4E-55594B2C50C4
-  Functions: 875
-  Symbols:   2888
-  CStrings:  1191
+  UUID: E3E8E674-52A3-3FA4-9BA9-A0EC02ECAA71
+  Functions: 874
+  Symbols:   2886
+  CStrings:  1194
 
Symbols:
+ -[PACoalescingIntervalState(Testing) hasActiveTransaction]
+ _OBJC_IVAR_$_PACoalescingIntervalState._activeTransaction
+ __OBJC_$_INSTANCE_METHODS_PACoalescingIntervalState(Testing)
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.134
- __OBJC_$_INSTANCE_METHODS_PACoalescingIntervalState
- __OBJC_$_PROP_LIST_PACoalescingIntervalState
- ___block_descriptor_56_e8_32bs40r48w_e5_v8?0lw48l8s32l8r40l8
- ___block_literal_global.128
Functions:
~ -[PACoalescingIntervalState initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:expiry:] : 668 -> 592
- ___Block_byref_object_copy_
~ ___107-[PACoalescingIntervalState initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:expiry:]_block_invoke : 116 -> 96
~ -[PACoalescingIntervalState .cxx_destruct] : 104 -> 116
- ___Block_byref_object_dispose_
+ -[PACoalescingIntervalState(Testing) hasActiveTransaction]
CStrings:
+ "@\"NSObject<OS_os_transaction>\""
+ "_activeTransaction"
+ "hasActiveTransaction"

```
