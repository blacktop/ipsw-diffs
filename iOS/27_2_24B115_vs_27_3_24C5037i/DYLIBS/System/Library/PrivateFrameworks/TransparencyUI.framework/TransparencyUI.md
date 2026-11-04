## TransparencyUI

> `/System/Library/PrivateFrameworks/TransparencyUI.framework/TransparencyUI`

```diff

-1766.40.58.0.0
-  __TEXT.__text: 0x3717c
-  __TEXT.__objc_methlist: 0x3074
-  __TEXT.__const: 0x5b2
-  __TEXT.__cstring: 0x4c66
-  __TEXT.__oslogstring: 0x2587
-  __TEXT.__gcc_except_tab: 0x3f4
+1766.60.7.0.0
+  __TEXT.__text: 0x37c50
+  __TEXT.__objc_methlist: 0x3094
+  __TEXT.__const: 0x5c2
+  __TEXT.__cstring: 0x4db6
+  __TEXT.__oslogstring: 0x2646
+  __TEXT.__gcc_except_tab: 0x488
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x521
   __TEXT.__swift5_reflstr: 0x46

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x18a0
+  __TEXT.__unwind_info: 0x1900
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc58
+  __DATA_CONST.__const: 0xcd0
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2148
+  __DATA_CONST.__objc_selrefs: 0x2168
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x818
-  __AUTH_CONST.__const: 0x2fc0
-  __AUTH_CONST.__cfstring: 0x1cc0
-  __AUTH_CONST.__objc_const: 0xa618
+  __AUTH_CONST.__const: 0x3080
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_const: 0xa698
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__auth_got: 0x608
   __AUTH.__objc_data: 0xe10
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x328
+  __DATA.__objc_ivar: 0x338
   __DATA.__data: 0x9c8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x190

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1972
-  Symbols:   2382
-  CStrings:  648
+  Functions: 1994
+  Symbols:   2402
+  CStrings:  658
 
Symbols:
+ -[TUIKTStateManager _computeState]
+ -[TUIKTStateManager fetchServerOptInIfNeeded:completion:]
+ -[TUIKTStateManager needsServerOptIn]
+ GCC_except_table116
+ GCC_except_table12
+ GCC_except_table124
+ GCC_except_table14
+ GCC_except_table180
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table210
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table8
+ _KTAccountStatusGetString
+ _KTOptInGetString
+ _OBJC_IVAR_$_TUIKTStateManager._effectiveAccountStatus
+ _OBJC_IVAR_$_TUIKTStateManager._effectiveOptIn
+ _OBJC_IVAR_$_TUIKTStateManager._serverOptIn
+ _OBJC_IVAR_$_TUIKTStateManager._serverOptInFetched
+ ___34-[TUIKTStateManager _computeState]_block_invoke
+ ___42-[TUIKTPaneViewController _checkKTStatus:]_block_invoke_3
+ ___43-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke_3
+ ___57-[TUIKTStateManager fetchServerOptInIfNeeded:completion:]_block_invoke
+ ___57-[TUIKTStateManager fetchServerOptInIfNeeded:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0Q8"NSError"16lw40l8s32l8
+ ___block_descriptor_57_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- GCC_except_table121
- GCC_except_table17
- GCC_except_table177
- GCC_except_table197
- GCC_except_table199
- GCC_except_table207
- GCC_except_table21
- GCC_except_table3
CStrings:
+ " (fetched)"
+ "%s asking KT server for opt-in state on %{public}@"
+ "%s forced account status %{public}@ on %{public}@"
+ "%s new %{public}@, serverOptIn %{public}@%{public}@ on %{public}@"
+ "%s server opt-in fetch failed: %{public}@ on %{public}@"
+ "-[TUIKTStateManager _computeState]"
+ "-[TUIKTStateManager fetchServerOptInIfNeeded:completion:]"
+ "-[TUIKTStateManager fetchServerOptInIfNeeded:completion:]_block_invoke"
+ "-[TUIKTStateManager fetchServerOptInIfNeeded:completion:]_block_invoke_2"
+ "-[TUIOptInSpecifierProvider _checkKTStatus]_block_invoke_2"
+ "v24@?0Q8@\"NSError\"16"
- "%s new %{public}@ on %{public}@"
```
