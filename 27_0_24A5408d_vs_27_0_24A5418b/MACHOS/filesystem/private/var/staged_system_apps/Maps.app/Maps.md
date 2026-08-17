## Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-2972.30.6.12.54
-  __TEXT.__text: 0x126653c
+2972.30.6.12.58
+  __TEXT.__text: 0x1268340
   __TEXT.__auth_stubs: 0xdc30
-  __TEXT.__objc_stubs: 0xf7c60
-  __TEXT.__objc_methlist: 0xbe2a0
-  __TEXT.__const: 0x46578
+  __TEXT.__objc_stubs: 0xf7d00
+  __TEXT.__objc_methlist: 0xbe300
+  __TEXT.__const: 0x46598
   __TEXT.__dlopen_cstrs: 0x174
   __TEXT.__constg_swiftt: 0x1af5c
-  __TEXT.__swift5_typeref: 0x53ae2
-  __TEXT.__cstring: 0x9dec6
-  __TEXT.__objc_methname: 0x18899f
-  __TEXT.__swift5_capture: 0xeb80
+  __TEXT.__swift5_typeref: 0x53b70
+  __TEXT.__cstring: 0x9df52
+  __TEXT.__objc_methname: 0x188a2f
+  __TEXT.__swift5_capture: 0xeb70
   __TEXT.__objc_classname: 0x22e89
-  __TEXT.__objc_methtype: 0x3ee05
+  __TEXT.__objc_methtype: 0x3ee35
   __TEXT.__swift5_builtin: 0xcbc
   __TEXT.__swift5_reflstr: 0x14f3f
   __TEXT.__swift5_fieldmd: 0x13314
   __TEXT.__swift5_assocty: 0x3ad0
-  __TEXT.__oslogstring: 0x74f73
+  __TEXT.__oslogstring: 0x7515d
   __TEXT.__swift5_proto: 0x1790
   __TEXT.__swift5_types: 0x14dc
-  __TEXT.__swift_as_entry: 0x714
-  __TEXT.__swift_as_ret: 0x7f4
-  __TEXT.__swift_as_cont: 0x11f4
+  __TEXT.__swift_as_entry: 0x718
+  __TEXT.__swift_as_ret: 0x7fc
+  __TEXT.__swift_as_cont: 0x1200
   __TEXT.__swift5_mpenum: 0x15c
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__gcc_except_tab: 0x18738
-  __TEXT.__ustring: 0x16b2
-  __TEXT.__unwind_info: 0x40b78
-  __TEXT.__eh_frame: 0x188e8
-  __DATA_CONST.__const: 0x75270
-  __DATA_CONST.__cfstring: 0x72be0
+  __TEXT.__ustring: 0x1a7e
+  __TEXT.__unwind_info: 0x40bc8
+  __TEXT.__eh_frame: 0x189e0
+  __DATA_CONST.__const: 0x75308
+  __DATA_CONST.__cfstring: 0x72cc0
   __DATA_CONST.__objc_classlist: 0x6478
   __DATA_CONST.__objc_catlist: 0x650
   __DATA_CONST.__objc_protolist: 0x2fa8

   __DATA_CONST.__auth_got: 0x6e30
   __DATA_CONST.__got: 0x8b38
   __DATA_CONST.__auth_ptr: 0x4828
-  __DATA.__objc_const: 0x165a18
-  __DATA.__objc_selrefs: 0x4b010
-  __DATA.__objc_ivar: 0xd63c
+  __DATA.__objc_const: 0x165a48
+  __DATA.__objc_selrefs: 0x4b038
+  __DATA.__objc_ivar: 0xd640
   __DATA.__objc_data: 0x56088
-  __DATA.__data: 0x446f0
+  __DATA.__data: 0x44730
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x32828
   __DATA.__common: 0x14d0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 97214
+  Functions: 97235
   Symbols:   7997
-  CStrings:  94039
+  CStrings:  94056
 
CStrings:
+ "Close Button Safety Check"
+ "ContaineeViewControllerReconcilePresentationOnDismiss"
+ "Open a place card first, then force the model↔UIKit orphan. Both reproduce real field states with the card's delegate intact/nil as it would be in the field: “context lingers” empties the owning context's card stack; “context popped” removes the context. With the safety check ON the x button closes the card and restores a clean state (selection cleared, contexts tidied); with it OFF the card is force-quit-only."
+ "Orphan place card — context lingers"
+ "Orphan place card — context popped"
+ "Reconcile presentation on dismiss"
+ "[%{public}@] debug orphan: collapsed internal stack to root. internal=%@ uikit=%@"
+ "[%{public}@] debug orphan: need a card on top of the root containee (open a place card first); nothing to orphan"
+ "[%{public}@] presentation state (%{public}@): contexts=%{public}@ internal=%{public}@ uikit=%{public}@"
+ "_closeButtonTapped"
+ "_debug_collapseInternalStackToRoot"
+ "_debug_emptyCardStack"
+ "_debug_removeTopContextWithoutTeardown"
+ "_internal_logPresentationStateForReason:"
+ "_internal_presentationStackAppearsCorrect"
+ "anyLaunchAlertNeedsAcknowledgement: YES (notification prewarm, shouldPrompt=%{bool}d, shouldRepeat=%{bool}d, authorizationStatus=%ld)"
+ "anyLaunchAlertNeedsAcknowledgement: notification prewarm due but will not present (shouldPrompt=%{bool}d, shouldRepeat=%{bool}d, authorizationStatus=%ld)"
+ "orphaned place card close"
- "anyLaunchAlertNeedsAcknowledgement: YES (notification prewarm, shouldPrompt=%{bool}d, shouldRepeat=%{bool}d)"
```
