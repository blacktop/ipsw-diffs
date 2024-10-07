## SwiftData

> `/System/Library/Frameworks/SwiftData.framework/SwiftData`

```diff

-89.1.0.0.0
-  __TEXT.__text: 0x111ba0
+90.2.0.0.0
+  __TEXT.__text: 0x111538
   __TEXT.__auth_stubs: 0x2730
   __TEXT.__objc_methlist: 0x114
-  __TEXT.__cstring: 0x6878
+  __TEXT.__cstring: 0x6808
   __TEXT.__const: 0x6aa8
   __TEXT.__constg_swiftt: 0x4b60
-  __TEXT.__swift5_typeref: 0x2dd2
+  __TEXT.__swift5_typeref: 0x2dc4
   __TEXT.__swift5_reflstr: 0x1cd5
   __TEXT.__swift5_fieldmd: 0x2264
   __TEXT.__swift5_builtin: 0x104

   __TEXT.__swift5_assocty: 0x5c8
   __TEXT.__swift5_proto: 0x4c8
   __TEXT.__swift5_types: 0x224
-  __TEXT.__oslogstring: 0x9a3
+  __TEXT.__oslogstring: 0xab3
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__unwind_info: 0x3a18

   __AUTH.__data: 0xcb0
   __DATA.__data: 0x1210
   __DATA.__bss: 0x6870
-  __DATA.__common: 0x40
+  __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x288
   __DATA_DIRTY.__data: 0x3f08
   __DATA_DIRTY.__bss: 0x2b10
-  __DATA_DIRTY.__common: 0x158
+  __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5138
+  Functions: 5137
   Symbols:   382
-  CStrings:  920
+  CStrings:  919
 
CStrings:
+ "ModelActor was deinitialized while ModelContext has unsaved changes.  This violates the non-Sendable isolation scope of the ModelContext.  The ModelActor should be strongly reference for as long as the ModelContext is in use.  This will be a hard error in Swift 6."
- "Failed to generate a fresh composite attribute from "
- "Other element is not a composite - "

```
