## MediaControl

> `/System/Library/PrivateFrameworks/MediaControl.framework/Versions/A/MediaControl`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-4026.100.75.0.0
-  __TEXT.__text: 0xbbce4
+4026.100.79.0.0
+  __TEXT.__text: 0xbbc4c
   __TEXT.__objc_methlist: 0x84
-  __TEXT.__const: 0x17810
+  __TEXT.__const: 0x17830
   __TEXT.__swift5_typeref: 0x297b
   __TEXT.__swift5_capture: 0x200c
-  __TEXT.__oslogstring: 0x18ee
+  __TEXT.__oslogstring: 0x19fe
   __TEXT.__constg_swiftt: 0x3fbc
   __TEXT.__swift5_reflstr: 0x1712
   __TEXT.__swift5_fieldmd: 0x3dfc

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8636
+  Functions: 8639
   Symbols:   2302
-  CStrings:  291
+  CStrings:  293
 
CStrings:
+ "[%{public}s] updatePendingItems - value: %{public}s"
+ "[%{public}s] updateSnapshot - value: %{public}s"
+ "[%{public}s] updateSnapshot - value: nil"
+ "[%{public}s]<%{public}s> beginInteractionWithControl<%{public}s> - control: %{public}s"
+ "[%{public}s]<%{public}s> beginInteractionWithControl<%{public}s> - control: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> connect - failed with error: %{public}@."
+ "[%{public}s]<%{public}s> deinit"
+ "[%{public}s]<%{public}s> endContinuousInteraction<%{public}s> missing finalizer. Was this interaction ended multiple times?"
+ "[%{public}s]<%{public}s> endContinuousInteractionWithControl<%{public}s> - control: %{public}s"
+ "[%{public}s]<%{public}s> endContinuousInteractionWithControl<%{public}s> - control: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> flushPendingVolumeControls - failed with error: %{public}@"
+ "[%{public}s]<%{public}s> handleAbsoluteVolumeControl - control: %{public}s value adjusted from: %{public}f to: %{public}f"
+ "[%{public}s]<%{public}s> handleAbsoluteVolumeControl - deferred control: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> handleInteractWithControlResult - deferred control: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> handleInteractWithControlResult - processed control: %{public}s, dispatch pending control: %{public}s"
+ "[%{public}s]<%{public}s> init"
+ "[%{public}s]<%{public}s> interactWithAction - action: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> interactWithControl - control: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> interactWithItem - item: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> interactWithSession - session: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> updateServiceExpandedSessionIdentifiers - value: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> updateServiceRoutingMode - value: %{public}s failed with error: %{public}@"
+ "[%{public}s]<%{public}s> updateServiceUIPresented - value: %{bool,public}d failed with error: %{public}@"
- "[%s] updatePendingItems - value: %{public}s"
- "[%s] updateSnapshot - value: %s"
- "[%s] updateSnapshot - value: nil"
- "[%s]<%s> interactWithControl - control: %{public}s failed with error: %{public}@"
- "[%s]<%s> updateServiceRoutingMode - value: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> beginInteractionWithControl<%{public}s> - control: %{public}s"
- "[%s]<%{public}s> beginInteractionWithControl<%{public}s> - control: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> connect - failed with error: %{public}@."
- "[%s]<%{public}s> endContinuousInteraction<%{public}s> missing finalizer. Was this interaction ended multiple times?"
- "[%s]<%{public}s> endContinuousInteractionWithControl<%{public}s> - control: %{public}s"
- "[%s]<%{public}s> endContinuousInteractionWithControl<%{public}s> - control: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> flushPendingVolumeControls - failed with error: %{public}@"
- "[%s]<%{public}s> handleAbsoluteVolumeControl - control: %{public}s value adjusted from: %{public}f to: %{public}f"
- "[%s]<%{public}s> handleAbsoluteVolumeControl - deferred control: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> handleInteractWithControlResult - deferred control: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> handleInteractWithControlResult - processed control: %{public}s, dispatch pending control: %{public}s"
- "[%s]<%{public}s> interactWithAction - action: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> interactWithItem - item: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> interactWithSession - session: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> updateServiceExpandedSessionIdentifiers - value: %{public}s failed with error: %{public}@"
- "[%s]<%{public}s> updateServiceUIPresented - value: %{bool,public}d failed with error: %{public}@"
```
