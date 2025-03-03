## libSEUpdater.dylib

> `/usr/lib/updaters/libSEUpdater.dylib`

```diff

-56.3.2.0.0
-  __TEXT.__text: 0x553c8
-  __TEXT.__auth_stubs: 0x1210
+56.4.13.0.0
+  __TEXT.__text: 0x56270
+  __TEXT.__auth_stubs: 0x1240
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x4ec
-  __TEXT.__const: 0x4f98
-  __TEXT.__oslogstring: 0x5e
-  __TEXT.__cstring: 0x7ca2
-  __TEXT.__gcc_except_tab: 0x7168
+  __TEXT.__objc_methlist: 0x654
+  __TEXT.__const: 0x4fa0
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__oslogstring: 0x5e
+  __TEXT.__cstring: 0x7ee9
+  __TEXT.__gcc_except_tab: 0x732c
+  __TEXT.__unwind_info: 0x1738
   __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methname: 0x125d
-  __TEXT.__objc_methtype: 0x7a9
+  __TEXT.__objc_methname: 0x1263
+  __TEXT.__objc_methtype: 0x799
   __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x570
+  __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x918
-  __AUTH_CONST.__const: 0x2af8
-  __AUTH_CONST.__cfstring: 0x2120
-  __AUTH_CONST.__objc_const: 0xb90
+  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__const: 0x2ad0
+  __AUTH_CONST.__cfstring: 0x2140
+  __AUTH_CONST.__objc_const: 0x8f0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x260
-  __DATA.__bss: 0x90
   __DATA.__common: 0x18
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1179
-  Symbols:   1571
-  CStrings:  1473
+  Functions: 1181
+  Symbols:   1582
+  CStrings:  1490
 
Symbols:
+ _NfRestoreInvalidateProhibitTimer
+ __ZNSt13exception_ptr31__from_native_exception_pointerEPv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
+ ___cxa_init_primary_exception
+ _objc_release_x9
- __ZSt17current_exceptionv
CStrings:
+ "At SLAMDeleteSEAppletTool"
+ "At SLAMLoadAndInstallSEAppletTool_0_0_2"
+ "DeleteSEAppletTool"
+ "Install SEAppletTool: %s\n"
+ "InstallSEAppletTool"
+ "Invalidated prohibit timer with rc %d\n"
+ "LoadAndInstallSEAppletTool"
+ "Platform Category %d is unknown in script with name %s"
+ "SLAMDeleteSEAppletTool"
+ "SLAMLoadAndInstallSEAppletTool_0_0_2"
+ "SLAMMigrateCopernicus_2_3_11"
+ "SLAMMigrateCopernicus_2_3_11_LoadAndInstallSunsprite_2_1_7"
+ "Skip DeleteSEAppletTool by SE chip type\n"
+ "Skip DeleteSEAppletTool by key\n"
+ "Skip LoadAndInstallSEAppletTool by SE chip type\n"
+ "Skip LoadAndInstallSEAppletTool by key\n"
+ "Successfully deleted SEAppletTool\n"
+ "Successfully loaded and installed SEAppletTool\n"
+ "invalidateProhibitTimer"
+ "prepareLazily"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@0:8"
- "SLAMMigrateCopernicus_2_2_8"
- "SLAMMigrateCopernicus_2_2_8_LoadAndInstallSunsprite_2_1_7"
- "prepare"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16@0:8"

```
