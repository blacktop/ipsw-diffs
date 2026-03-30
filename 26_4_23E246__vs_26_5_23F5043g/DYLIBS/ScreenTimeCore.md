## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.4.18.1.0
-  __TEXT.__text: 0xc4140
+605.5.5.0.0
+  __TEXT.__text: 0xc4334
   __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0x9360
-  __TEXT.__const: 0x2410
-  __TEXT.__cstring: 0x9cbc
-  __TEXT.__oslogstring: 0x9faf
+  __TEXT.__objc_methlist: 0x9380
+  __TEXT.__const: 0x2400
+  __TEXT.__cstring: 0x9ccc
+  __TEXT.__oslogstring: 0xa01f
   __TEXT.__gcc_except_tab: 0x1c34
   __TEXT.__constg_swiftt: 0x8d0
   __TEXT.__swift5_typeref: 0xbb2

   __TEXT.__unwind_info: 0x3068
   __TEXT.__eh_frame: 0x16e0
   __TEXT.__objc_classname: 0x1e50
-  __TEXT.__objc_methname: 0x193e0
+  __TEXT.__objc_methname: 0x19450
   __TEXT.__objc_methtype: 0x2b51
   __TEXT.__objc_stubs: 0xe240
   __DATA_CONST.__got: 0xbf0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f20
+  __DATA_CONST.__objc_selrefs: 0x4f38
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb28
   __AUTH_CONST.__const: 0x1d50
-  __AUTH_CONST.__cfstring: 0x9480
-  __AUTH_CONST.__objc_const: 0x11b28
+  __AUTH_CONST.__cfstring: 0x94a0
+  __AUTH_CONST.__objc_const: 0x11b58
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x3398
   __AUTH.__data: 0x340
-  __DATA.__objc_ivar: 0x744
+  __DATA.__objc_ivar: 0x748
   __DATA.__data: 0x1b08
   __DATA.__bss: 0x36d0
   __DATA.__common: 0x68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1478BF55-8756-3E81-A84A-0D8E740F663E
-  Functions: 4776
-  Symbols:   12603
-  CStrings:  7342
+  UUID: 7EF5FDC4-7DA4-3017-800F-8A6F531C0FF0
+  Functions: 4779
+  Symbols:   12614
+  CStrings:  7351
 
Symbols:
+ +[STBlueprint(Downtime) disableDowntimeBlueprintForUser:error:]
+ +[STBlueprint(Downtime) disableDowntimeBlueprintForUser:error:].cold.1
+ +[STBlueprint(Downtime) disableDowntimeBlueprintForUser:error:].cold.2
+ -[STIntroductionModel setShouldDisableDowntime:]
+ -[STIntroductionModel shouldDisableDowntime]
+ _OBJC_IVAR_$_STIntroductionModel._shouldDisableDowntime
CStrings:
+ "Failed to disable downtime schedule: %{public}@"
+ "Failed to save after disabling downtime blueprint: %{public}@"
+ "ShouldDisableDowntime"
+ "TB,N,V_shouldDisableDowntime"
+ "_shouldDisableDowntime"
+ "disableDowntimeBlueprintForUser:error:"
+ "setShouldDisableDowntime:"
+ "shouldDisableDowntime"

```
