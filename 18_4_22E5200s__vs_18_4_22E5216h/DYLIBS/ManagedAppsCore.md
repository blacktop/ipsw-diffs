## ManagedAppsCore

> `/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore`

```diff

-20.4.13.0.0
-  __TEXT.__text: 0x6d9e8
+20.4.16.0.0
+  __TEXT.__text: 0x791a4
   __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x3fc
-  __TEXT.__const: 0x4130
-  __TEXT.__cstring: 0x2287
-  __TEXT.__constg_swiftt: 0x118c
-  __TEXT.__swift5_typeref: 0x129e
-  __TEXT.__swift5_reflstr: 0x96b
-  __TEXT.__swift5_fieldmd: 0xb24
-  __TEXT.__oslogstring: 0x12c2
-  __TEXT.__swift5_capture: 0x440
+  __TEXT.__objc_methlist: 0x418
+  __TEXT.__const: 0x4230
+  __TEXT.__cstring: 0x23d7
+  __TEXT.__constg_swiftt: 0x11b4
+  __TEXT.__swift5_typeref: 0x12c4
+  __TEXT.__swift5_reflstr: 0x9bb
+  __TEXT.__swift5_fieldmd: 0xb48
+  __TEXT.__oslogstring: 0x1432
+  __TEXT.__swift5_capture: 0x480
   __TEXT.__swift5_proto: 0x218
   __TEXT.__swift5_types: 0xbc
-  __TEXT.__swift_as_entry: 0x16c
-  __TEXT.__swift_as_ret: 0x15c
+  __TEXT.__swift_as_entry: 0x184
+  __TEXT.__swift_as_ret: 0x174
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1728
-  __TEXT.__eh_frame: 0x438c
+  __TEXT.__unwind_info: 0x1820
+  __TEXT.__eh_frame: 0x4a3c
   __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methname: 0xa64
+  __TEXT.__objc_methname: 0xa84
   __TEXT.__objc_methtype: 0x4d6
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d8
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x30
   __AUTH_CONST.__auth_got: 0xaa0
-  __AUTH_CONST.__auth_ptr: 0x6a0
-  __AUTH_CONST.__const: 0x1ab8
-  __AUTH_CONST.__objc_const: 0x1968
+  __AUTH_CONST.__auth_ptr: 0x5b0
+  __AUTH_CONST.__const: 0x1b40
+  __AUTH_CONST.__objc_const: 0x1990
   __AUTH.__objc_data: 0x3f8
-  __AUTH.__data: 0x17e0
-  __DATA.__data: 0xfb8
-  __DATA.__bss: 0x3fa0
+  __AUTH.__data: 0x1810
+  __DATA.__data: 0x1018
+  __DATA.__bss: 0x3fb0
   __DATA.__common: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1922
+  Functions: 1986
   Symbols:   220
-  CStrings:  455
+  CStrings:  471
 
Symbols:
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "%s - app record has no bundleID"
+ "%s - recordID: %s"
+ "%{public}s"
+ "%{public}s - Failed to cleanup pending removal %{public}s: %{public}s"
+ "%{public}s - Found pending removal %{public}s"
+ "%{public}s - could not read legacy app config from file: %{public}@"
+ "%{public}s - managementKey: %{public}s"
+ "%{public}s - managementKey: %{public}s, appCodeIdentity: %s extensions: %ld"
+ "%{public}s - managementKey: %{public}s, bundleID: %{public}s"
+ "%{public}s - no result for record %{public}s"
+ "%{public}s - no result for record %{public}s!"
+ "%{public}s - record: %s"
+ "%{public}s - setAppConfig:\n%s"
+ ", pendingRemoval "
+ "Failed to complete removal of app config info with error: "
+ "_pendingRemoval"
+ "completeRemovalOfAppConfig(for:)"
+ "completeRemovalOfAppConfigFor::"
+ "pendingRemovalCleanUp()"
+ "removeAppRecord(recordID:)"
+ "startUpMaintenance()"
+ "updateAppRecord(managementKey:updateBlock:)"
+ "updateAppRecord(record:updateBlock:)"
+ "updateAppRecord(recordID:updateBlock:)"
- "%s"
- "%s - could not read legacy app config from file: %{public}@"
- "%s - managementKey: %s, appCodeIdentity: %s extensions: %ld"
- "%s - managementKey: %s, bundleID: %s"
- "%s - setAppConfig:\n%s"
- "%{public}s - no result for record %s!"
- "removeAppRecord(_:)"
- "updateAppRecord(_:updateBlock:)"

```
