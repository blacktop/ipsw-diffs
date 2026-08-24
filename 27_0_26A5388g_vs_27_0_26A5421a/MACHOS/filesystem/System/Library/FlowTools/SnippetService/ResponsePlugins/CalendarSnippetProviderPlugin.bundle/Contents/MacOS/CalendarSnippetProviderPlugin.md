## CalendarSnippetProviderPlugin

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/CalendarSnippetProviderPlugin.bundle/Contents/MacOS/CalendarSnippetProviderPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-3600.18.5.0.0
-  __TEXT.__text: 0x14370
-  __TEXT.__auth_stubs: 0xad0
+3600.18.9.14.1
+  __TEXT.__text: 0x1adb0
+  __TEXT.__auth_stubs: 0xc80
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0x850
-  __TEXT.__cstring: 0xeb
+  __TEXT.__const: 0x9e0
+  __TEXT.__cstring: 0xfb
   __TEXT.__objc_classname: 0x7d
   __TEXT.__objc_methname: 0x9e
   __TEXT.__objc_methtype: 0x24
-  __TEXT.__constg_swiftt: 0x1a8
-  __TEXT.__swift5_typeref: 0x30e
-  __TEXT.__swift5_reflstr: 0x8d
-  __TEXT.__swift5_fieldmd: 0x140
-  __TEXT.__swift5_capture: 0xc0
-  __TEXT.__oslogstring: 0x5b5
-  __TEXT.__swift5_proto: 0x20
-  __TEXT.__swift5_types: 0x2c
+  __TEXT.__constg_swiftt: 0x214
+  __TEXT.__swift5_typeref: 0x3a0
+  __TEXT.__swift5_reflstr: 0xbd
+  __TEXT.__swift5_fieldmd: 0x1b8
+  __TEXT.__oslogstring: 0x9c5
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x98
-  __TEXT.__swift_as_cont: 0x50
-  __TEXT.__swift_as_ret: 0x74
+  __TEXT.__swift_as_cont: 0x58
+  __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift5_capture: 0xb0
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x410
-  __TEXT.__eh_frame: 0x9c8
-  __DATA_CONST.__const: 0x4a8
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__eh_frame: 0xb78
+  __DATA_CONST.__const: 0x510
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x1a8
+  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__auth_ptr: 0x228
   __DATA.__objc_const: 0x190
   __DATA.__objc_selrefs: 0x38
-  __DATA.__data: 0x478
-  __DATA.__common: 0x70
-  __DATA.__bss: 0x400
+  __DATA.__data: 0x648
+  __DATA.__common: 0x88
+  __DATA.__bss: 0x500
   - /System/Library/Frameworks/EventKit.framework/Versions/A/EventKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CalendarUIKit.framework/Versions/A/CalendarUIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 341
-  Symbols:   98
-  CStrings:  39
+  Functions: 402
+  Symbols:   103
+  CStrings:  51
 
Symbols:
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getEnumCaseMultiPayload
+ _swift_storeEnumTagMultiPayload
CStrings:
+ "DeleteEventIntent"
+ "[CalendarSnippetProvider] Building event from entity on the synchronous per-item path — no hydration, so eventModel and punch-out are unavailable (idiom=%{public}s)"
+ "[CreateEventSnippetHandler] Extracted %ld created events from response"
+ "[CreateEventSnippetHandler] Failed to hydrate any events from %ld entities"
+ "[EventConfirmationHandler] Calendar event `.confirm` from an unhandled tool — schemaId=%{public}s, toolId=%{public}s"
+ "[EventConfirmationHandler] Calendar event `.confirm` without an actionConfirmation context (kind=%{public}s)"
+ "[EventConfirmationHandler] EventEntity not found in the typedValue passed to handle (operation=%{public}s): %s"
+ "[Snippet.Event] CalendarEntity color is not a symbolic palette color"
+ "[Snippet.Event] CalendarEntity missing color parameter"
+ "[Snippet.Event] EntityValue location parameter in an unhandled shape"
+ "[Snippet.Event] EntityValue missing title parameter"
+ "[Snippet.Event] Unknown symbolic calendar color"
+ "[Snippet.Event] hydrate(): EKEphemeralCacheEventStoreProvider returned a nil store; rendering placeholder data"
+ "parameterConfirmation"
- "[DeleteEventConfirmationHandler] EventEntity not found in the typedValue passed to handle: %s"
- "com.apple.mobilecal.DeleteEventIntent"
```
