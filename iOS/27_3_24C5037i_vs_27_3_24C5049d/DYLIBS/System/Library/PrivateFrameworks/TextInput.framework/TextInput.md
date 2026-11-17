## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3568.2.4.0.0
-  __TEXT.__text: 0x7dfc4
-  __TEXT.__objc_methlist: 0xb780
+3568.2.8.0.0
+  __TEXT.__text: 0x7e6a4
+  __TEXT.__objc_methlist: 0xb820
   __TEXT.__dlopen_cstrs: 0x459
   __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x4964b
+  __TEXT.__cstring: 0x49661
   __TEXT.__ustring: 0xc8bd8
-  __TEXT.__oslogstring: 0xb19
-  __TEXT.__unwind_info: 0x2a50
+  __TEXT.__oslogstring: 0xbeb
+  __TEXT.__unwind_info: 0x2a70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24c8
+  __DATA_CONST.__const: 0x24f0
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5720
+  __DATA_CONST.__objc_selrefs: 0x5790
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0x101a90
+  __DATA_CONST.__objc_arraydata: 0x101aa8
   __DATA_CONST.__got: 0x620
   __AUTH_CONST.__const: 0xdc0
-  __AUTH_CONST.__cfstring: 0x255e20
-  __AUTH_CONST.__objc_const: 0x11f20
+  __AUTH_CONST.__cfstring: 0x255e40
+  __AUTH_CONST.__objc_const: 0x11fb8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x50a0
   __AUTH_CONST.__objc_dictobj: 0xf1b8

   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__auth_got: 0x800
   __AUTH.__objc_data: 0x2710
-  __DATA.__objc_ivar: 0xb90
+  __DATA.__objc_ivar: 0xb9c
   __DATA.__data: 0xcf0
   __DATA_DIRTY.__objc_data: 0x1310
-  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__bss: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4037
-  Symbols:   7720
-  CStrings:  76816
+  Functions: 4052
+  Symbols:   7739
+  CStrings:  76819
 
Symbols:
+ +[TIKeyboardCandidate prefersArchivedResultSetCoding]
+ +[TIKeyboardCandidateResultSet _archivedCandidatesFromData:]
+ +[TIKeyboardCandidateResultSetCoder decodeWithData:archivedCandidates:]
+ +[TIKeyboardCandidateResultSetCoder encodeWithCandidateResultSet:archivedCandidates:]
+ -[TIKeyboardCandidateResultSetCoder archivedCandidates]
+ -[TIKeyboardCandidateResultSetCoder encodeCandidate:]
+ -[TIKeyboardCandidateResultSetCoder encodedCandidateCount]
+ -[TIKeyboardCandidateResultSetCoder replacementCandidates]
+ -[TIKeyboardCandidateResultSetCoder setArchivedCandidates:]
+ -[TIKeyboardCandidateResultSetCoder setEncodedCandidateCount:]
+ -[TIKeyboardCandidateResultSetCoder setReplacementCandidates:]
+ -[TIPreferencesController isPreferenceKeyDisallowedByRestrictions:]
+ -[TIPreferencesController shouldSuppressEnglishCandidates]
+ -[TIPreferencesController shouldSuppressPredictionCandidates]
+ _OBJC_IVAR_$_TIKeyboardCandidateResultSetCoder._archivedCandidates
+ _OBJC_IVAR_$_TIKeyboardCandidateResultSetCoder._encodedCandidateCount
+ _OBJC_IVAR_$_TIKeyboardCandidateResultSetCoder._replacementCandidates
+ ___60+[TIKeyboardCandidateResultSet _archivedCandidatesFromData:]_block_invoke
+ ___block_descriptor_40_8_32s_e15_v32?0816^B24ls32l8
CStrings:
+ "Could not archive candidates of a candidate result set: domain=%{public}@ code=%{public}ld: %{private}@"
+ "Could not unarchive candidates of a candidate result set: domain=%{public}@ code=%{public}ld: %{private}@"
+ "archivedCandidates"
```
