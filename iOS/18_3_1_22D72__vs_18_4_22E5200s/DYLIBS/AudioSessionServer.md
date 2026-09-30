## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-321.401.0.0.0
-  __TEXT.__text: 0x5b844
+321.516.0.0.0
+  __TEXT.__text: 0x5a668
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x6d0
-  __TEXT.__const: 0xb79
-  __TEXT.__gcc_except_tab: 0x86d8
-  __TEXT.__cstring: 0x426e
+  __TEXT.__objc_methlist: 0xb78
+  __TEXT.__const: 0xb99
+  __TEXT.__gcc_except_tab: 0x8164
+  __TEXT.__cstring: 0x422d
   __TEXT.__oslogstring: 0x38b4
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2658
+  __TEXT.__unwind_info: 0x25a0
   __TEXT.__objc_classname: 0x13a
   __TEXT.__objc_methname: 0x1955
-  __TEXT.__objc_methtype: 0x291d
+  __TEXT.__objc_methtype: 0x28dd
   __TEXT.__objc_stubs: 0xe40
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__const: 0x490
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x658
+  __DATA_CONST.__objc_selrefs: 0x6f8
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__const: 0x9f8
+  __AUTH_CONST.__const: 0x9b0
   __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x1488
+  __AUTH_CONST.__objc_const: 0xb98
   __AUTH_CONST.__objc_intobj: 0x78
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x249

   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x2b8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1415
-  Symbols:   2096
-  CStrings:  1246
+  Functions: 1364
+  Symbols:   2057
+  CStrings:  1245
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
+ _memcpy
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[AVAudioSessionRemoteXPCClient getDeferredMessages:reply:]_block_invoke"
+ "@80@0:8@16{ProcessInfo={ProcessToken=I}@@{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}24@72"
+ "{ProcessInfo=\"token\"{ProcessToken=\"mValue\"I}\"xpcConnection\"@\"NSXPCConnection\"\"mClientRelay\"@\"AVAudioSessionXPCClientRelay\"\"mProcessName\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}}"
+ "{tuple<int, std::string, int>={__tuple_impl<std::__tuple_indices<0, 1, 2>, int, std::string, int>=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}i}}20@0:8I16"
- "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]_block_invoke_2"
- "@80@0:8@16{ProcessInfo={ProcessToken=I}@@{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}24@72"
- "Unknown Interruption"
- "{ProcessInfo=\"token\"{ProcessToken=\"mValue\"I}\"xpcConnection\"@\"NSXPCConnection\"\"mClientRelay\"@\"AVAudioSessionXPCClientRelay\"\"mProcessName\"{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"{__rep=\"\"(?=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1}\"__r\"{__raw=\"__words\"[3Q]})}}}}"
- "{tuple<int, std::string, int>={__tuple_impl<std::__tuple_indices<0, 1, 2>, int, std::string, int>=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}i}}20@0:8I16"

```
