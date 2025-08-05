## UIGrounding

> `/System/Library/PrivateFrameworks/UIGrounding.framework/UIGrounding`

```diff

-13.3.0.0.0
-  __TEXT.__text: 0x1b9a8
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__const: 0x1fb8
-  __TEXT.__cstring: 0xa06
-  __TEXT.__constg_swiftt: 0x968
-  __TEXT.__swift5_typeref: 0x624
+14.0.0.0.0
+  __TEXT.__text: 0x1c384
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__const: 0x2138
+  __TEXT.__cstring: 0xa36
+  __TEXT.__constg_swiftt: 0x9b0
+  __TEXT.__swift5_typeref: 0x65e
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x536
-  __TEXT.__swift5_fieldmd: 0x9ac
-  __TEXT.__swift5_proto: 0x1d4
-  __TEXT.__swift5_types: 0xac
+  __TEXT.__swift5_fieldmd: 0x9e4
+  __TEXT.__swift5_proto: 0x1ec
+  __TEXT.__swift5_types: 0xb4
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__oslogstring: 0xcd
-  __TEXT.__unwind_info: 0x9a0
-  __TEXT.__eh_frame: 0x1238
+  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__eh_frame: 0x1298
   __TEXT.__objc_methname: 0x138
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x810
-  __AUTH_CONST.__const: 0x1470
+  __AUTH_CONST.__auth_got: 0x828
+  __AUTH_CONST.__const: 0x1580
   __AUTH_CONST.__objc_const: 0x988
   __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0xa30
-  __DATA.__data: 0x610
-  __DATA.__bss: 0x3a80
+  __AUTH.__data: 0xa38
+  __DATA.__data: 0x650
+  __DATA.__bss: 0x3d80
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 351241B5-AEEF-3B7F-8D7E-CB79660A9884
-  Functions: 762
-  Symbols:   370
+  UUID: 66DB3734-AE3B-32E7-8E18-29A7BFBB225D
+  Functions: 784
+  Symbols:   378
   CStrings:  104
 
Symbols:
+ _associated conformance 11UIGrounding20ModelResponseMessageV10CodingKeys33_28456B448A22478985ACEB176AC3C737LLOSHAASQ
+ _associated conformance 11UIGrounding20ModelResponseMessageV10CodingKeys33_28456B448A22478985ACEB176AC3C737LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11UIGrounding20ModelResponseMessageV10CodingKeys33_28456B448A22478985ACEB176AC3C737LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _symbolic _____ 11UIGrounding20ModelResponseMessageV
+ _symbolic _____ 11UIGrounding20ModelResponseMessageV10CodingKeys33_28456B448A22478985ACEB176AC3C737LLO
+ _symbolic _____Sg 10Foundation6LocaleV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11UIGrounding20ModelResponseMessageV10CodingKeys33_28456B448A22478985ACEB176AC3C737LLO
+ _type_layout_string 11UIGrounding20ModelResponseMessageV
CStrings:
+ "Your answer must be exclusively in this JSON format: {\"action\": <action type from below>}\nDo not include additional text.\nAvailable actions:\ntap (click an element): {\"type\": \"tap\", \"element_id\": <int id of element>}\nswipe (to scroll or view more options): {\"type\": \"swipe\", \"direction\": \"up|down|left|right\"}\ntextentry (enter text into an element): {\"type\": \"textentry\", \"element_id\": <int id of element>, \"text\": \"text string to enter\"}\nstop (unable to execute action on this screen): {\"type\": \"stop\", \"details\": \"reason action cannot be performed\"}"
- "Your answer must be in this JSON format only: {\"action\": <action type from below>}\nAvailable actions:\ntap (click an element): {\"type\": \"tap\", \"element_id\": <int id of element>}\nswipe (to scroll or view more options): {\"type\": \"swipe\", \"direction\": \"up|down|left|right\"}\ntextentry (enter text into an element): {\"type\": \"textentry\", \"element_id\": <int id of element>, \"text\": \"text string to enter\"}\nstop (unable to execute action on this screen): {\"type\": \"stop\", \"details\": \"reason action cannot be performed\"}"

```
