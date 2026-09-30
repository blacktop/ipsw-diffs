## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

 101.0.0.0.0
-  __TEXT.__text: 0x928bc
-  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__text: 0x92894
+  __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x53f4
+  __TEXT.__cstring: 0x5292
   __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__const: 0x1d78
   __TEXT.__objc_methname: 0x13b
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x378
-  __DATA_CONST.__auth_got: 0x5a8
+  __TEXT.__unwind_info: 0x370
+  __DATA_CONST.__auth_got: 0x5a0
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x430

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0BB4FD4B-E023-3A05-8FF2-F6943F24911A
+  UUID: 85524064-0AA4-38C1-B443-034E52C59222
   Functions: 293
-  Symbols:   762
-  CStrings:  663
+  Symbols:   761
+  CStrings:  662
 
Symbols:
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIl15sqliteDBState_tEENS_22__unordered_map_hasherIlNS_4pairIKlS2_EENS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS7_SB_S9_Lb1EEENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE : 112 -> 68
~ _____library_initializer_block_invoke : 68 -> 72
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJmBugD469oCnTuPX1LJ4llqaY5fLbwXkYOQcFU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"

```
