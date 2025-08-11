## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-1027.12.0.0.0
-  __TEXT.__text: 0x1045d8
+1027.13.0.0.0
+  __TEXT.__text: 0x1049ac
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_stubs: 0x10dc0
-  __TEXT.__objc_methlist: 0xd8ec
+  __TEXT.__objc_stubs: 0x10e00
+  __TEXT.__objc_methlist: 0xd904
   __TEXT.__const: 0x688
   __TEXT.__gcc_except_tab: 0x2694
-  __TEXT.__objc_methname: 0x1c1cd
-  __TEXT.__cstring: 0xdaca
-  __TEXT.__oslogstring: 0x158f9
+  __TEXT.__objc_methname: 0x1c215
+  __TEXT.__cstring: 0xdae7
+  __TEXT.__oslogstring: 0x15a53
   __TEXT.__objc_classname: 0x225b
-  __TEXT.__objc_methtype: 0x49be
+  __TEXT.__objc_methtype: 0x49c9
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x3a58
+  __TEXT.__unwind_info: 0x3a60
   __DATA_CONST.__auth_got: 0x888
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x4a00
-  __DATA_CONST.__cfstring: 0xbc40
+  __DATA_CONST.__cfstring: 0xbc60
   __DATA_CONST.__objc_classlist: 0x7c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA.__objc_const: 0x19f80
-  __DATA.__objc_selrefs: 0x5de8
+  __DATA.__objc_selrefs: 0x5df8
   __DATA.__objc_ivar: 0x11cc
   __DATA.__objc_data: 0x4dd0
   __DATA.__data: 0x19d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: CC921EF6-7116-3E14-BD67-8600ECEFA7D1
-  Functions: 5758
+  UUID: 9E2DD168-2B2D-3069-8F4F-621B72C8B45D
+  Functions: 5760
   Symbols:   696
-  CStrings:  10164
+  CStrings:  10173
 
CStrings:
+ "259"
+ "EPMobileAssetAutoTrigger: Cooldown has not elapsed (%.0f seconds remaining); deferring scan"
+ "EPMobileAssetAutoTrigger: Last update check interval: %.0f seconds"
+ "EPMobileAssetAutoTrigger: Update failed, failure count now: %ld"
+ "EPMobileAssetAutoTrigger: Using %d second interval for success or invalid failure count"
+ "EPMobileAssetAutoTrigger: Using backoff interval: %.0f seconds for failure count: %ld"
+ "EPMobileAssetAutoTrigger: setLastAssetUpdateCheckDate: %{public}@ withSuccess: %@"
+ "NanoRegistry-1027.13"
+ "d24@0:8q16"
+ "getFailureCount"
+ "getRequiredCooldownIntervalForFailureCount:"
+ "lastAssetUpdateFailureCount"
+ "setLastAssetUpdateCheckDate:withSuccess:"
- "34"
- "EPMobileAssetAutoTrigger: Cooldown has not elapsed; deferring scan"
- "EPMobileAssetAutoTrigger: setLastAssetUpdateCheckDate: %{public}@"
- "NanoRegistry-1027.12"
- "setLastAssetUpdateCheckDate:"

```
