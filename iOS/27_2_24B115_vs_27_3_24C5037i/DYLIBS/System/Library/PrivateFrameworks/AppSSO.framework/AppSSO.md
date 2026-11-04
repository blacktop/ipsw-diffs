## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-643.40.34.0.0
-  __TEXT.__text: 0x2b5e0
-  __TEXT.__objc_methlist: 0x1c54
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x19a4
-  __TEXT.__oslogstring: 0x4ce8
-  __TEXT.__cstring: 0x383c
+643.60.12.0.0
+  __TEXT.__text: 0x2bcdc
+  __TEXT.__objc_methlist: 0x1c9c
+  __TEXT.__const: 0x160
+  __TEXT.__gcc_except_tab: 0x19b0
+  __TEXT.__oslogstring: 0x4da1
+  __TEXT.__cstring: 0x3960
   __TEXT.__dlopen_cstrs: 0x6dc
-  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__unwind_info: 0x1300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd70
+  __DATA_CONST.__const: 0xd98
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1318
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x240
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1340
-  __AUTH_CONST.__objc_const: 0x4900
+  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__objc_const: 0x4950
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x174
+  __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x6d0
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x1d8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1068
-  Symbols:   1490
-  CStrings:  735
+  Functions: 1077
+  Symbols:   1501
+  CStrings:  745
 
Symbols:
+ -[SOExtension _failRegisteredDelegatesWithMessage:]
+ -[SOExtension _resetFailedRequestIdentifiers]
+ -[SOExtension abandonRequestWithIdentifier:]
+ -[SOExtension attachAuthorizationViewControllerWithCompletion:]
+ -[SOExtension sessionSetupTimeout]
+ -[SOExtension setSessionSetupTimeout:]
+ GCC_except_table54
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table79
+ _OBJC_IVAR_$_SOExtension._failedRequestIdentifiers
+ _OBJC_IVAR_$_SOExtension._sessionSetupTimeout
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e5_B8?0lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56r_e28_v24?0"NSUUID"8"NSError"16ls32l8s40l8s48l8r56l8
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- GCC_except_table40
- GCC_except_table41
- GCC_except_table59
- GCC_except_table61
- GCC_except_table73
- GCC_except_table77
- ___block_descriptor_56_e8_32s40bs48r_e28_v24?0"NSUUID"8"NSError"16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s48l8s40l8
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
CStrings:
+ "-[SOExtension abandonRequestWithIdentifier:]"
+ "-[SOExtension attachAuthorizationViewControllerWithCompletion:]"
+ "Attaching a view controller is not supported on this platform"
+ "B8@?0"
+ "No remote extension context for the session"
+ "Timed out setting up a session for extension %{public}@ -- failing the request"
+ "Timed out setting up the extension session"
+ "extension session unloaded"
+ "failing %lu registered delegate(s): %{public}@"
+ "request %{public}@ already completed -- nothing to abandon"
```
