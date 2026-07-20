## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/Versions/A/AppPredictionInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-664.0.2.0.0
-  __TEXT.__text: 0x511d8c
-  __TEXT.__objc_methlist: 0x38a64
+667.0.0.0.0
+  __TEXT.__text: 0x511e78
+  __TEXT.__objc_methlist: 0x38a74
   __TEXT.__const: 0x5ef0
-  __TEXT.__cstring: 0x59f54
-  __TEXT.__oslogstring: 0x3ad19
-  __TEXT.__gcc_except_tab: 0x10730
+  __TEXT.__cstring: 0x59e74
+  __TEXT.__oslogstring: 0x3adc9
+  __TEXT.__gcc_except_tab: 0x10708
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x1c4f

   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xf830
+  __TEXT.__unwind_info: 0xf838
   __TEXT.__eh_frame: 0x5fb4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1bdc8
+  __DATA_CONST.__objc_selrefs: 0x1bdd8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1488
   __DATA_CONST.__objc_arraydata: 0x1328
   __DATA_CONST.__got: 0x3b40
   __AUTH_CONST.__const: 0x13748
-  __AUTH_CONST.__cfstring: 0x3b2c0
+  __AUTH_CONST.__cfstring: 0x3b260
   __AUTH_CONST.__objc_const: 0x82858
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x3450

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26715
-  Symbols:   47172
-  CStrings:  12435
+  Functions: 26718
+  Symbols:   47176
+  CStrings:  12434
 
Symbols:
+ -[ATXModeEntityScorerServer _appBundleIdsThatCannotBeSuggested]
+ ATXSetInput
+ _objc_msgSend$_appBundleIdsThatCannotBeSuggested
+ _objc_msgSend$sectionSubtitle
CStrings:
+ "ATXSetInput: dropping NaN value for input %lu (\"%@\")"
+ "ATXSetInput: dropping infinite value %f for input %lu (\"%@\")"
+ "ATXSetInput: dropping out-of-range input type %lu (max %lu)"
- "Input type must be less than _ATXScoreInputMax: %lu >= %lu"
- "Value must be a number. currently nan (input %lu, \"%@\")"
- "Value must be finite (input %lu, \"%@\")"
- "void ATXSetInput(ATXPredictionItem * _Nonnull, _ATXScoreInput, double)"
```
