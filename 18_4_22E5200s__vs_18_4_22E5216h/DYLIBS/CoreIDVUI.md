## CoreIDVUI

> `/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI`

```diff

-7.415.1.0.0
-  __TEXT.__text: 0xd7de8
-  __TEXT.__auth_stubs: 0x3e80
+7.418.0.0.0
+  __TEXT.__text: 0xdbb60
+  __TEXT.__auth_stubs: 0x3ec0
   __TEXT.__objc_methlist: 0x1c88
-  __TEXT.__const: 0x33a4
+  __TEXT.__const: 0x33e4
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x7bf3
-  __TEXT.__oslogstring: 0x6079
+  __TEXT.__cstring: 0x7d63
+  __TEXT.__oslogstring: 0x64d9
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__constg_swiftt: 0x4dd8
-  __TEXT.__swift5_typeref: 0x36b6
+  __TEXT.__constg_swiftt: 0x4e78
+  __TEXT.__swift5_typeref: 0x36ea
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x3305
-  __TEXT.__swift5_fieldmd: 0x2284
+  __TEXT.__swift5_reflstr: 0x3375
+  __TEXT.__swift5_fieldmd: 0x22c0
   __TEXT.__swift5_assocty: 0x270
   __TEXT.__swift5_proto: 0x12c
   __TEXT.__swift5_types: 0x1d4
-  __TEXT.__swift5_capture: 0x115c
-  __TEXT.__swift_as_entry: 0x164
-  __TEXT.__swift_as_ret: 0x184
+  __TEXT.__swift5_capture: 0x1200
+  __TEXT.__swift_as_entry: 0x170
+  __TEXT.__swift_as_ret: 0x198
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x25b8
-  __TEXT.__eh_frame: 0x3694
+  __TEXT.__unwind_info: 0x2670
+  __TEXT.__eh_frame: 0x399c
   __TEXT.__objc_classname: 0x23a
-  __TEXT.__objc_methname: 0x5139
+  __TEXT.__objc_methname: 0x5140
   __TEXT.__objc_methtype: 0x16a1
   __TEXT.__objc_stubs: 0x920
-  __DATA_CONST.__got: 0xd58
+  __DATA_CONST.__got: 0xd60
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_selrefs: 0x1500
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1f50
-  __AUTH_CONST.__auth_ptr: 0xd20
-  __AUTH_CONST.__const: 0x4e68
+  __AUTH_CONST.__auth_got: 0x1f70
+  __AUTH_CONST.__auth_ptr: 0xdb8
+  __AUTH_CONST.__const: 0x50c8
   __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x6b78
-  __AUTH.__objc_data: 0x5920
-  __AUTH.__data: 0x3268
+  __AUTH_CONST.__objc_const: 0x6c18
+  __AUTH.__objc_data: 0x5988
+  __AUTH.__data: 0x32b8
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x24e0
+  __DATA.__data: 0x2510
   __DATA.__bss: 0x1e50
   __DATA.__common: 0x1a8
   __DATA_DIRTY.__objc_data: 0xbe8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3302
-  Symbols:   820
-  CStrings:  2105
+  Functions: 3356
+  Symbols:   834
+  CStrings:  2122
 
Symbols:
+ _dispatch_sync
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "Configuration doesn't exist for a given state and country. Cannot update views. "
+ "Country of the configuration unavailable. Cannot update the views. "
+ "FetchAndUpdateLatestProofingViews: We dont want to update the UI on fed stats optin view"
+ "FetchAndUpdateLatestProofingViews: Will update the proofing views"
+ "Internal setting for enableUIUpdateOnStatusChange is enabled. Will update UI when there is a proofing status change"
+ "RGBCaptureViewController takeLivePhotoStarted"
+ "Received an error during proofing view update %s"
+ "State of the configuration unavailable. Cannot update the views. "
+ "The Country of the identity document is %s"
+ "The state of the identity document is %s"
+ "activeConfiguration(status:state:country:)"
+ "currentProofingActionStatus"
+ "notifyActiveConfigurationChange: The action status is %s"
+ "notifyActiveConfigurationChange: The currentProofingActionStatus %s and the activeConfiguration.actionStatus %s are equal. No need to update the views. "
+ "notifyActiveConfigurationChange: Updating the UI by fetching the new views based on a different action status"
+ "notifyActiveConfigurationChange: currentProofingActionStatus is nil"
+ "notifyActiveConfigurationChange: notify active configurations changed invoked on the caller"
+ "notifyActiveConfigurationChange: received an error in checking the proofing status %s"
+ "notifyActiveConfigurationChange: the action status doesn't exist. Cannot continue with updating the views"
+ "setViewControllers:animated:"
+ "updateCurrentProofingActionStatus: Setting the CurrentProofingActionStatus to %s"
- "notify active configurations changed invoked on the caller"
- "proofing status doesn't exist. Cannot return the active configuration."
- "received an error in checking the proofing status %s"
- "setHyphenationFactor:"

```
