## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-  __TEXT.__text: 0x384cec
+  __TEXT.__text: 0x3866c0
   __TEXT.__auth_stubs: 0x2a40
   __TEXT.__objc_stubs: 0x48e0
   __TEXT.__objc_methlist: 0xedc

   __TEXT.__swift5_proto: 0xb34
   __TEXT.__swift5_types: 0x5c4
   __TEXT.__swift5_capture: 0x5cdc
-  __TEXT.__oslogstring: 0x1d6e9
-  __TEXT.__cstring: 0x41c9
+  __TEXT.__oslogstring: 0x1d909
+  __TEXT.__cstring: 0x4229
   __TEXT.__swift_as_entry: 0x444
   __TEXT.__swift_as_ret: 0x5d4
   __TEXT.__swift5_protos: 0x210
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7088
-  __TEXT.__eh_frame: 0xf174
+  __TEXT.__unwind_info: 0x7080
+  __TEXT.__eh_frame: 0xf144
   __DATA_CONST.__auth_got: 0x1528
   __DATA_CONST.__got: 0x1068
   __DATA_CONST.__auth_ptr: 0x1320

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9052
+  Functions: 9055
   Symbols:   1390
-  CStrings:  3884
+  CStrings:  3893
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__objc_stublist : content changed
~ __DATA.__bss : content changed
CStrings:
+ "Configuration value at %s has unexpected type %s; defaulting to false"
+ "Couldn't find configuration value at %s in the url bag"
+ "Custodian handleFailedSetup failed for custodianID: %s, error: %@"
+ "Custodian not tearing down setup; teardownActionEnabled is false for custodianID: %s"
+ "Owner handleFailedSetup failed for custodianID: %s, error: %@"
+ "Owner not tearing down setup; teardownActionEnabled is false for custodianID: %s"
+ "ownerSetupGracePeriodV2InSeconds"
+ "teardownActionEnabled"
+ "🔔 Internal build: %s override is set to: %{bool}d"

```
