## MediaSuggester

> `/System/Library/PrivateFrameworks/MediaSuggester.framework/MediaSuggester`

```diff

-67.4.0.0.0
-  __TEXT.__text: 0x5bfe8
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0xfdc
-  __TEXT.__const: 0x3144
-  __TEXT.__cstring: 0x1c84
-  __TEXT.__swift5_typeref: 0x163a
-  __TEXT.__constg_swiftt: 0x15c0
+67.6.0.0.0
+  __TEXT.__text: 0x6198c
+  __TEXT.__auth_stubs: 0x1310
+  __TEXT.__objc_methlist: 0x1054
+  __TEXT.__const: 0x3214
+  __TEXT.__cstring: 0x1d74
+  __TEXT.__swift5_typeref: 0x165e
+  __TEXT.__constg_swiftt: 0x166c
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x1509
+  __TEXT.__swift5_reflstr: 0x15a9
   __TEXT.__swift5_assocty: 0x700
-  __TEXT.__swift5_capture: 0x554
-  __TEXT.__oslogstring: 0x13ac
+  __TEXT.__swift5_capture: 0x5c0
+  __TEXT.__oslogstring: 0x188c
   __TEXT.__swift5_proto: 0x198
-  __TEXT.__swift5_types: 0xe4
-  __TEXT.__swift5_fieldmd: 0xcd8
+  __TEXT.__swift5_types: 0xe8
+  __TEXT.__swift5_fieldmd: 0xd6c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift_as_entry: 0x11c
-  __TEXT.__swift_as_ret: 0x10c
-  __TEXT.__unwind_info: 0x1858
-  __TEXT.__eh_frame: 0x2a9c
-  __TEXT.__objc_classname: 0xb0b
-  __TEXT.__objc_methname: 0x2243
+  __TEXT.__swift_as_entry: 0x13c
+  __TEXT.__swift_as_ret: 0x12c
+  __TEXT.__unwind_info: 0x1978
+  __TEXT.__eh_frame: 0x2d84
+  __TEXT.__objc_classname: 0xb2b
+  __TEXT.__objc_methname: 0x23d3
   __TEXT.__objc_methtype: 0xaf4
-  __TEXT.__objc_stubs: 0x1400
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x190
-  __DATA_CONST.__objc_classlist: 0x190
+  __TEXT.__objc_stubs: 0x15a0
+  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x798
+  __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x998
-  __AUTH_CONST.__const: 0x2040
+  __AUTH_CONST.__auth_got: 0x990
+  __AUTH_CONST.__const: 0x2158
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x3508
-  __AUTH.__objc_data: 0xc08
-  __AUTH.__data: 0x1c50
-  __DATA.__data: 0xc50
+  __AUTH_CONST.__objc_const: 0x36e8
+  __AUTH.__objc_data: 0xd80
+  __AUTH.__data: 0x1c70
+  __DATA.__data: 0xcf0
   __DATA.__bss: 0x3380
   __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x3d0

   __DATA_DIRTY.__common: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/Intents.framework/Intents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE59A41F-B912-34E6-8D1E-A8C469A7C7AA
-  Functions: 2604
-  Symbols:   230
-  CStrings:  773
+  UUID: 231DB6B3-3443-373B-A86D-1882154AB39F
+  Functions: 2748
+  Symbols:   238
+  CStrings:  816
 
Symbols:
+ _OBJC_CLASS_$_INImage
+ _OBJC_CLASS_$_LNActionMetadata
+ _OBJC_CLASS_$_LNEntityIdentifier
+ _OBJC_CLASS_$_LNEntityValueType
+ _OBJC_CLASS_$_LNValue
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_MSPlayMediaAppEntity
+ _OBJC_METACLASS_$_MSPlayMediaAppEntity
CStrings:
+ " actionIdentifier="
+ ", entityTypeAndIdentifier="
+ "Action identifier '%s' not found for %s; falling back to %s"
+ "Bundle ID not found on current platform: %s"
+ "Bundle ID valid on current platform, no translation: %s"
+ "Checking counterpartIdentifiers for third-party app: %s"
+ "Could not execute App Entity: %s. No valid bundleID"
+ "Could not execute App Intent: %s. No valid bundleID"
+ "Executed App Entity: (id: %@"
+ "Executing App Entity: %s using bundleID: %s"
+ "Executing App Entity: (id: %s [compatibility path - no bundleID translation]"
+ "Executing App Entity: (id: %s with stored bundle ID: %s"
+ "Executing App Intent: (id: %s with stored bundle ID: %s"
+ "First-party fallback: %s → %s"
+ "Found counterpart via LSApplicationRecord: %s → %s"
+ "LNAction.execute() called (compatibility path) - delegating to executeWithStoredBundleID(\"\")"
+ "MSIntentWrapper decode FAILED: intent or bundleID missing"
+ "MSIntentWrapper executionBlock failed with error: %@"
+ "MSPlayMediaAppEntity"
+ "MSUnifiedMediaIntent.execute() async completed with error: %@"
+ "MSUnifiedMediaIntent.execute() completed with error: %@"
+ "MediaSuggester.MSPlayMediaAppEntity"
+ "No action metadata found for %s with identifiers '%s' or '%s'"
+ "No bundle ID provided for App Entity: %s"
+ "No bundle ID provided for App Intent: %s"
+ "No translation found, using original bundle ID: %s"
+ "Unable to create LNEntityIdentifier from: %s"
+ "actionIdentifier"
+ "actionsForBundleIdentifier:andActionIdentifier:error:"
+ "bundleIdentifier"
+ "counterpartIdentifiers"
+ "entityIdentifier"
+ "entityTypeAndIdentifier"
+ "enumeratorWithOptions:"
+ "executeWithStoredBundleID(_:)"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithIdentifier:"
+ "initWithIdentifier:value:"
+ "initWithString:"
+ "initWithTypeIdentifier:bundleIdentifier:instanceIdentifier:"
+ "initWithValue:valueType:displayRepresentation:"
+ "nextObject"
+ "setPreferredBundleIdentifier:"
+ "typeAndIdentifier"
- "Could not executing App Intent: %s. Invalid bundleID: %s"
- "Error executing intent: %@"
- "Executing App Intent: (id: %s"

```
