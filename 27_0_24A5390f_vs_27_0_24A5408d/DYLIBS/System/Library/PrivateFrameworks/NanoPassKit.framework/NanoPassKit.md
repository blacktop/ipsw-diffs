## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1341.0.0.0.0
-  __TEXT.__text: 0x1e9d88
-  __TEXT.__objc_methlist: 0x1ff28
-  __TEXT.__cstring: 0x12c84
-  __TEXT.__const: 0x2f0
+1347.0.0.0.0
+  __TEXT.__text: 0x1ea8bc
+  __TEXT.__objc_methlist: 0x1ffa8
+  __TEXT.__cstring: 0x12cd4
+  __TEXT.__const: 0x300
   __TEXT.__gcc_except_tab: 0x3808
-  __TEXT.__oslogstring: 0x22813
+  __TEXT.__oslogstring: 0x22879
   __TEXT.__dlopen_cstrs: 0x1ba
   __TEXT.__ustring: 0x168
   __TEXT.__constg_swiftt: 0x28

   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x7480
+  __TEXT.__unwind_info: 0x7498
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8eb8
+  __DATA_CONST.__objc_selrefs: 0x8f00
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xf20
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x1610
+  __DATA_CONST.__got: 0x1620
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0xa9a0
-  __AUTH_CONST.__objc_const: 0x36e88
+  __AUTH_CONST.__cfstring: 0xaa00
+  __AUTH_CONST.__objc_const: 0x36f20
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x8d90
-  __DATA.__objc_ivar: 0x16b0
+  __DATA.__objc_ivar: 0x16b8
   __DATA.__data: 0x1120
   __DATA.__bss: 0x1a8
   __DATA_DIRTY.__objc_data: 0xd20

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11907
-  Symbols:   21441
-  CStrings:  3749
+  Functions: 11919
+  Symbols:   21460
+  CStrings:  3754
 
Symbols:
+ +[NPKGizmoDatabase passByPreservingDeviceOwnedSettingsFromExisting:onIncoming:]
+ +[NSDictionary(NPKRelevancy) npkRelevancyTupleWithUniqueID:relevantText:reasonText:shouldSuppressLiveActivity:]
+ -[NPKProtoRelevantPassTuple hasReasonText]
+ -[NPKProtoRelevantPassTuple reasonText]
+ -[NPKProtoRelevantPassTuple setReasonText:]
+ -[NPKRelevancyInformation hash]
+ -[NPKRelevancyInformation initWithPassUniqueID:groupID:relevantText:reasonText:shouldSuppressLiveActivity:]
+ -[NPKRelevancyInformation isEqual:]
+ -[NPKRelevancyInformation reasonText]
+ -[NSDictionary(NPKRelevancy) npkRelevancyReasonText]
+ -[PKPass(NanoPassKit) npkSupportsRelevancy]
+ GCC_except_table154
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table288
+ _NPKNRDeviceSupportsSEPassRelevancy
+ _NPKPairedOrPairingDeviceSupportsSEPassRelevancy
+ _NPKPassByPreservingDeviceOwnedSettings
+ _OBJC_IVAR_$_NPKProtoRelevantPassTuple._reasonText
+ _OBJC_IVAR_$_NPKRelevancyInformation._reasonText
+ _PKIdentityTypesSupportingRelevancy
+ _PKPassLibraryRelevantInfoBodyText
+ ___block_descriptor_56_e8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
+ _objc_msgSend$hasTimeOrLocationRelevancyInfo
+ _objc_msgSend$isStoredValuePass
+ _objc_msgSend$setReasonText:
- +[NSDictionary(NPKRelevancy) npkRelevancyTupleWithUniqueID:relevantText:shouldSuppressLiveActivity:]
- -[NPKRelevancyInformation initWithPassUniqueID:groupID:relevantText:shouldSuppressLiveActivity:]
- GCC_except_table153
- GCC_except_table193
- GCC_except_table197
- GCC_except_table199
- GCC_except_table201
- GCC_except_table205
- GCC_except_table207
- GCC_except_table211
- GCC_except_table213
- GCC_except_table215
- GCC_except_table217
- GCC_except_table219
- GCC_except_table221
- GCC_except_table229
- GCC_except_table231
- GCC_except_table234
- GCC_except_table258
- GCC_except_table276
- GCC_except_table284
- GCC_except_table42
- ___block_descriptor_48_e8_32s40s_e5_B8?0ls32l8s40l8
CStrings:
+ "<%@: %p\n\tpassUniqueID: %@\n\tgroupID: %@\n\trelevantText: %@\n\treasonText: %@\n\tshouldSuppressLiveActivity: %@\n>"
+ "BuildVersion"
+ "IdentityStreamlinedPresentment"
+ "Notice: Preserving device-owned settings 0x%llx for %@ across content save"
+ "Notice: Target check fido key presence for relayingParty %{private}@ accountHash %{private}@ fidoKeyHash %{private}@ completion %@"
+ "Notice: Target create fido key for relying party %{private}@ accountHash %{private}@ challenge %{private}@ externalizedauth %{private}@ with completion %@"
+ "Notice: Target sign with fido key for relaying party %{private}@ accountHash %{private}@ fidoKeyHash %{private}@ challenge %{private}@ publicKeyIdentifier %{private}@ externalizedAuth %{private}@ completion %@"
+ "[%@] %@"
+ "reasonText"
- "<%@: %p\n\tpassUniqueID: %@\n\tgroupID: %@\n\trelevantText: %@\n\tshouldSuppressLiveActivity: %@\n>"
- "Notice: Target check fido key presence for relayingParty %@ accountHash %{private}@ fidoKeyHash %{private}@ completion %@"
- "Notice: Target create fido key for relying party %@ accountHash %{private}@ challenge %{private}@ externalizedauth %{private}@ with completion %@"
- "Notice: Target sign with fido key for relaying party %@ accountHash %{private}@ fidoKeyHash %{private}@ challenge %{private}@ publicKeyIdentifier %{private}@ externalizedAuth %{private}@ completion %@"
```
