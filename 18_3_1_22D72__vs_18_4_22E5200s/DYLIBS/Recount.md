## Recount

> `/System/Library/PrivateFrameworks/Recount.framework/Recount`

```diff

-15.0.0.0.0
-  __TEXT.__text: 0x384e4
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__const: 0x2e90
-  __TEXT.__cstring: 0x1433
-  __TEXT.__swift5_typeref: 0xd7b
-  __TEXT.__constg_swiftt: 0xbe0
-  __TEXT.__swift5_reflstr: 0x978
-  __TEXT.__swift5_fieldmd: 0x1154
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_mpenum: 0x8c
-  __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_proto: 0x310
-  __TEXT.__swift5_types: 0x140
+34.100.0.502.1
+  __TEXT.__text: 0x42f2c
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0x5d6a
+  __TEXT.__cstring: 0x14a7
+  __TEXT.__swift5_typeref: 0x129c
+  __TEXT.__constg_swiftt: 0x113c
+  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__swift5_mpenum: 0xb4
+  __TEXT.__swift5_reflstr: 0xc17
+  __TEXT.__swift5_fieldmd: 0x1968
+  __TEXT.__swift5_proto: 0x52c
+  __TEXT.__swift5_types: 0x1d4
+  __TEXT.__oslogstring: 0x34b
+  __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__oslogstring: 0x35
-  __TEXT.__unwind_info: 0x1108
-  __TEXT.__eh_frame: 0x1b40
+  __TEXT.__unwind_info: 0x13b0
+  __TEXT.__eh_frame: 0x29f8
   __TEXT.__objc_classname: 0x35
-  __TEXT.__objc_methname: 0x1fc
+  __TEXT.__objc_methname: 0x1b9
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x80
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__auth_ptr: 0x2f8
-  __AUTH_CONST.__const: 0x2f90
-  __AUTH_CONST.__objc_const: 0xa78
-  __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x680
-  __DATA.__data: 0xaa8
-  __DATA.__bss: 0x6110
+  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__auth_ptr: 0x358
+  __AUTH_CONST.__const: 0x4228
+  __AUTH_CONST.__objc_const: 0x1068
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0xb58
+  __DATA.__data: 0xee8
+  __DATA.__bss: 0xa490
   __DATA.__common: 0x98
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/kperf.framework/kperf

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1444
-  Symbols:   183
-  CStrings:  221
+  Functions: 1727
+  Symbols:   211
+  CStrings:  252
 
Symbols:
+ _kdebug_trace
+ _swift_copyKeyPathTrivialIndices
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getAtKeyPath
+ _swift_getErrorValue
+ _swift_makeBoxUnique
+ _swift_retain_n
- _fmod
- _memset
- _objc_retain_x20
- _os_variant_has_internal_content
CStrings:
+ " across all sets"
+ " and events on counters "
+ " configurable starting at "
+ " is missing a threshold value"
+ " is not a name of an expression for threshold "
+ " not found in mode for area display"
+ " not found in mode for bar display"
+ ") with settings "
+ ", configuration "
+ ", multiplexing period "
+ "/System/AppleInternal/Library/Recount/Analysis/"
+ ": failed to create expression from "
+ ": failed to decode mode: "
+ ": mode is unsupported on "
+ "Awimbo PMC configured sampling on context-switch"
+ "Awimbo PMC configured sampling on timer with period %{public}s"
+ "Awimbo PMC starting KPC configuration with %{public}s"
+ "Awimbo PMI using KPC configuration %{public}s"
+ "Awimbo PMI using events %{public}s, period %{public}s from %{public}s"
+ "CPUCountersProvider"
+ "CounterAnalysis named "
+ "CountingMode named "
+ "CountingMode.Settings for "
+ "KPC settings with config: "
+ "RECOUNT_ANALYSIS_PATH"
+ "_TtC7Recount12CountingMode"
+ "_TtC7Recount15CounterAnalysis"
+ "_TtC7Recount15EventDictionary"
+ "_TtC7Recount8Platform"
+ "_TtCC7Recount12CountingMode6Metric"
+ "_TtCC7Recount12CountingMode9Threshold"
+ "applying %{public}s failed: %{public}s"
+ "commentary"
+ "constants"
+ "could not find CounterAnalysis named %{public}s"
+ "denominator"
+ "displays"
+ "documentation"
+ "elements"
+ "evaluator"
+ "eventDictionary"
+ "expected `normalized-area' or `bar' for display kind, not `"
+ "failed to decode CounterAnalysis from URL %{public}s for %{public}s: %{public}s"
+ "failed to decode CounterAnalysis: %{public}s"
+ "failed to encode %{public}s: %{public}s"
+ "failed to evaluate metric values: %{public}s"
+ "id"
+ "initialModeID"
+ "initialized %{public}s"
+ "initialized %{public}s with %{public}ld expressions, %{public}ld constants"
+ "kind"
+ "limits"
+ "metric"
+ "namedExpressions"
+ "nextCountingMode"
+ "nextCountingModeID"
+ "parsing options %{public}s"
+ "platform"
+ "resultCount"
+ "searching in %{public}s for CounterAnalysis specifications"
+ "spec"
+ "suggestedMaximum"
+ "supportedCountingModes"
+ "synopsis"
+ "thresholds"
- "/AppleInternal/System/Library/Recount/Modes/"
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Placing events at %s"
- "RECOUNT_MODES_PATH"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_TtC7Recount10EventStore"
- "configs: %s, samplers: %s"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "displayCommentary"
- "displayDescription"
- "displayDocumentation"
- "displayName"
- "invalid Collection: less than 'count' elements in collection"
- "missing expression for "
- "supportedPlatforms"

```
