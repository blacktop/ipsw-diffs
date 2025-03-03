## Lexicon

> `/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon`

```diff

-173.4.2.0.0
-  __TEXT.__text: 0xdbfb8
-  __TEXT.__auth_stubs: 0x1620
+173.7.0.0.0
+  __TEXT.__text: 0xddc74
+  __TEXT.__auth_stubs: 0x1660
   __TEXT.__objc_methlist: 0x94
-  __TEXT.__const: 0xe50f
+  __TEXT.__const: 0xe51f
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__gcc_except_tab: 0xaeb4
-  __TEXT.__cstring: 0x960c
+  __TEXT.__gcc_except_tab: 0xb070
+  __TEXT.__cstring: 0x9620
   __TEXT.__oslogstring: 0x19db
   __TEXT.__ustring: 0x98e
-  __TEXT.__unwind_info: 0x4cd8
+  __TEXT.__unwind_info: 0x4d28
   __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methname: 0x21c
   __TEXT.__objc_methtype: 0x237
   __TEXT.__objc_stubs: 0x1e0
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__const: 0x1828
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb20
+  __AUTH_CONST.__auth_got: 0xb40
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x9bc8
   __AUTH_CONST.__cfstring: 0x1360

   __AUTH.__thread_bss: 0x2300
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x89
-  __DATA.__bss: 0x528
+  __DATA.__bss: 0x538
   __DATA.__common: 0x10
   __DATA_DIRTY.__bss: 0x3a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libgermantok.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4299
-  Symbols:   588
-  CStrings:  1317
+  Functions: 4309
+  Symbols:   592
+  CStrings:  1319
 
Symbols:
+ _CFStringGetCharacterAtIndex
+ _germantok_tokenize
+ _objc_release_x26
+ _objc_release_x9
+ _u_getNumericValue
- _objc_release_x24
CStrings:
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/cedarpp.h"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1146: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1148: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1162: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1167: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1385: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1731: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1733: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1748: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:708: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:847: exception: failed to build rank index: std::bad_alloc"
+ "length > 0"
+ "tokenize"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/cedarpp.h"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1146: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1148: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1162: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1167: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1385: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1731: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1733: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:1748: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:708: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/trie/darts_clone.h:847: exception: failed to build rank index: std::bad_alloc"

```
