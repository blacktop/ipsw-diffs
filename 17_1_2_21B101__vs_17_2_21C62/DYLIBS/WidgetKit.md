## WidgetKit

> `/System/Library/Frameworks/WidgetKit.framework/WidgetKit`

```diff

-401.12.100.0.0
-  __TEXT.__text: 0x14eaa8
-  __TEXT.__auth_stubs: 0x3b30
+402.23.100.0.0
+  __TEXT.__text: 0x14e3fc
+  __TEXT.__auth_stubs: 0x3b60
   __TEXT.__objc_methlist: 0x564
-  __TEXT.__const: 0xed80
-  __TEXT.__cstring: 0x6cb6
+  __TEXT.__const: 0xed90
+  __TEXT.__cstring: 0x6ce6
   __TEXT.__swift5_typeref: 0x6a92
-  __TEXT.__swift5_reflstr: 0x2a81
+  __TEXT.__swift5_reflstr: 0x2aa1
   __TEXT.__swift5_assocty: 0xf98
   __TEXT.__constg_swiftt: 0x68e0
-  __TEXT.__swift5_fieldmd: 0x3bf4
+  __TEXT.__swift5_fieldmd: 0x3c0c
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_proto: 0xb10
   __TEXT.__swift5_types: 0x5a4
-  __TEXT.__swift5_capture: 0x14c4
+  __TEXT.__swift5_capture: 0x14d4
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x676c
-  __TEXT.__eh_frame: 0x5c88
+  __TEXT.__unwind_info: 0x6708
+  __TEXT.__eh_frame: 0x5c28
   __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x14a9
+  __TEXT.__objc_methname: 0x1494
   __TEXT.__objc_methtype: 0x10e
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0xec8
+  __DATA_CONST.__got: 0xec0
   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4628
-  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_selrefs: 0x620
   __AUTH_CONST.__objc_const: 0x390
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__const: 0xf370
-  __AUTH_CONST.__auth_got: 0x1da0
+  __AUTH_CONST.__auth_got: 0x1db8
   __AUTH.__data: 0x2e98
   __AUTH.__objc_data: 0x480
   __DATA.__objc_protorefs: 0x50
   __DATA.__objc_classrefs: 0x1d0
   __DATA.__objc_data: 0x2f0
-  __DATA.__data: 0x51f0
+  __DATA.__data: 0x5200
   __DATA.__bss: 0x7890
-  __DATA.__common: 0x109
+  __DATA.__common: 0x119
   __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__data: 0x4fe0
+  __DATA_DIRTY.__data: 0x4fc8
   __DATA_DIRTY.__common: 0x5b0
   __DATA_DIRTY.__bss: 0xd080
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 05732BAF-E3F5-37B7-8DCB-8B30686AF4F2
-  Functions: 9063
+  UUID: FB9B75BA-4D2A-3CDC-AC14-C9386297253A
+  Functions: 9064
   Symbols:   2926
   CStrings:  911
 
CStrings:
+ "%s - remoteObjectProxy error: %@"
+ "%{public}s - error reloading all timelines: %{public}@"
+ "%{public}s - error reloading supported intents: %{public}@"
+ "%{public}s - error reloading timelines of kind '%{public}s': %{public}@"
+ "%{public}s - remoteObjectProxy error: %{public}@"
+ "%{public}s Session operation: `%{public}s` error result: %@"
+ "%{public}s Unexpected error on session: %{public}@"
+ "%{public}s unable to acquire %{public}s error: %{public}@"
+ "Batch begin (%{public}s) - locale: %{public}s"
+ "Batch end (%{public}s) - failure: %{public}@"
+ "Batch end (%{public}s) - success"
+ "Batch ended (%{public}s) - failure: %{public}@"
+ "Batch ended (%{public}s) - success"
+ "Error decoding activity attributes: %s: %@"
+ "Error decoding activity state: %s: %@"
+ "Request ended for %{public}s - error: %@"
+ "Unable to acquire runtime assertion for WidgetArchiver.unarchive - error: %{public}@"
+ "[%{public}s] Unable to create new WidgetExtensionSession because begin request failed: %{public}@"
+ "[%{public}s] Unable to create new WidgetExtensionSession due to extension identity error: %{public}@"
+ "containsInteractiveControls"
- "%s - remoteObjectProxy error: %s"
- "%{public}s - error reloading all timelines: %{public}s"
- "%{public}s - error reloading supported intents: %{public}s"
- "%{public}s - error reloading timelines of kind '%{public}s': %{public}s"
- "%{public}s - remoteObjectProxy error: %{public}s"
- "%{public}s Session operation: `%{public}s` error result: %s"
- "%{public}s Unexpected error on session: %{public}s"
- "%{public}s unable to acquire %{public}s error: %{public}s"
- "Batch begin - locale: %{public}s"
- "Batch end - failure: %{public}s - %{public}s"
- "Batch end - success"
- "Batch ended - failure: %{public}s - %{public}s"
- "Batch ended - success"
- "Error decoding activity attributes: %s: %s"
- "Error decoding activity state: %s: %s"
- "Request ended for %{public}s - error: %{public}s - %{public}s"
- "Unable to acquire runtime assertion for WidgetArchiver.unarchive - error: %{public}s"
- "[%{public}s] Unable to create new WidgetExtensionSession because begin request failed: %{public}s"
- "[%{public}s] Unable to create new WidgetExtensionSession due to extension identity error: %{public}s"
- "localizedDescription"

```
