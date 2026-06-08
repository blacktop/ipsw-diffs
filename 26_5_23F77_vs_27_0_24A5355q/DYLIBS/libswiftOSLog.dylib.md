## libswiftOSLog.dylib

> `/usr/lib/swift/libswiftOSLog.dylib`

```diff

 10.0.0.0.0
   __TEXT.__text: 0x56c
-  __TEXT.__auth_stubs: 0x130
   __TEXT.__swift5_typeref: 0x93
   __TEXT.__swift5_capture: 0x10
   __TEXT.__const: 0x1aa

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x88
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_methname: 0xb4
-  __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x18
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__auth_got: 0xa0
   __DATA.__data: 0x18
   __DATA.__bss: 0x80
   __DATA.__common: 0x1

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 40D18540-ADB5-3A73-A952-35A40D2553A7
+  UUID: D213663F-43B5-3CFA-A8BA-78413939909C
   Functions: 19
-  Symbols:   139
-  CStrings:  8
+  Symbols:   141
+  CStrings:  0
 
Symbols:
+ ___swift_closure_destructor
Functions:
~ sub_2a41bce50 -> _$sSo10OSLogStoreC0A0E15PrivateIterator33_A983D55EFF15D70AF9FA0E38A33507C0LLV4nextSo0A5EntryCSgyF : 56 -> 172
~ _$sSo10OSLogStoreC0A0E15PrivateIterator33_A983D55EFF15D70AF9FA0E38A33507C0LLV4nextSo0A5EntryCSgyF -> _$sSo10OSLogStoreC0A0E15PrivateIterator33_A983D55EFF15D70AF9FA0E38A33507C0LLVStACSt4next7ElementQzSgyFTW : 172 -> 44
~ _$sSo10OSLogStoreC0A0E15PrivateIterator33_A983D55EFF15D70AF9FA0E38A33507C0LLVStACSt4next7ElementQzSgyFTW -> _$sSo10OSLogStoreC0A0E10getEntries4with2at8matchings11AnySequenceVySo0A5EntryCGSo0A17EnumeratorOptionsV_So0A8PositionCSgSo11NSPredicateCSgtKF : 44 -> 272
~ _$sSo10OSLogStoreC0A0E10getEntries4with2at8matchings11AnySequenceVySo0A5EntryCGSo0A17EnumeratorOptionsV_So0A8PositionCSgSo11NSPredicateCSgtKF -> ___swift_closure_destructor : 272 -> 56
CStrings:
- "argumentCategory"
- "argumentDataValue"
- "argumentDoubleValue"
- "argumentInt64Value"
- "argumentStringValue"
- "argumentUInt64Value"
- "entriesEnumeratorWithOptions:position:predicate:error:"
- "nextObject"

```
