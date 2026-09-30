## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper`

```diff

-1827.1.12.0.0
-  __TEXT.__text: 0x5f154
-  __TEXT.__auth_stubs: 0x1620
+1827.2.1.0.0
+  __TEXT.__text: 0x6db90
+  __TEXT.__auth_stubs: 0x17d0
   __TEXT.__objc_stubs: 0x1ce0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x78c
-  __TEXT.__gcc_except_tab: 0x847c
-  __TEXT.__cstring: 0x179a
-  __TEXT.__const: 0x1340
-  __TEXT.__oslogstring: 0x1340
+  __TEXT.__gcc_except_tab: 0x8e1c
+  __TEXT.__cstring: 0x1b40
+  __TEXT.__const: 0x1810
+  __TEXT.__oslogstring: 0x13c8
   __TEXT.__objc_classname: 0x123
   __TEXT.__ustring: 0x1a
   __TEXT.__objc_methname: 0x1bc3
   __TEXT.__objc_methtype: 0xeb3
-  __TEXT.__unwind_info: 0x2bc0
-  __DATA_CONST.__auth_got: 0xb20
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1458
+  __TEXT.__unwind_info: 0x3078
+  __DATA_CONST.__auth_got: 0xbf8
+  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__const: 0x1bc0
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_data: 0x230
   __DATA.__data: 0x448
   __DATA.__common: 0x1be
-  __DATA.__bss: 0x520
+  __DATA.__bss: 0x880
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CDA05681-6F3E-31DE-9366-E6CC3AC112AE
-  Functions: 1547
-  Symbols:   521
-  CStrings:  912
+  UUID: 083952E4-DDA5-33CB-83E2-95640C328461
+  Functions: 1778
+  Symbols:   557
+  CStrings:  946
 
Symbols:
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm
+ __ZNKSt3__123__match_any_but_newlineIcE6__execERNS_7__stateIcEE
+ __ZNKSt3__16locale4nameEv
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__18ios_base6getlocEv
+ __ZNSt3__111regex_errorC1ENS_15regex_constants10error_typeE
+ __ZNSt3__111regex_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEi
+ __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__115__get_classnameEPKcb
+ __ZNSt3__120__get_collation_nameEPKc
+ __ZNSt3__15ctypeIcE2idE
+ __ZNSt3__16localeC1ERKS0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__17collateIcE2idE
+ __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
+ __ZNSt3__18ios_base4initEPv
+ __ZNSt3__18ios_base5clearEj
+ __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZTINSt3__111regex_errorE
+ __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ _memchr
+ _memset
CStrings:
+ "\n"
+ "%%"
+ "%-@"
+ "%@"
+ "%[0-9]*\\.[0-9]+s"
+ "%d"
+ "%d (%{public}s)"
+ "%f"
+ "%p"
+ "%s"
+ "%x"
+ "%{private}@"
+ "%{public}-@"
+ "%{public}@"
+ "%{public}s"
+ "%{}"
+ "'N/A'"
+ "(%([{](public|private)[}])?[+\\- #0]?(([0-9]+)|[\\\\*])?(\\.(([0-9]+)|[\\*]))?(hh|h|ll|l|j|z|t|L)?[diu])(.|\\n)*"
+ "(%([{](public|private)[}])?[+\\- #0]?(([0-9]+)|[\\\\*])?(\\.(([0-9]+)|[\\*]))?(hh|h|ll|l|j|z|t|L)?[diuoxXfFeEgGaAcspn@])(.|\\n)*"
+ "(%([{](public|private)[}])?[+\\- #0]?(([0-9]+)|[\\\\*])?(\\.(([0-9]+)|[\\*]))?(hh|h|ll|l|j|z|t|L)?[fFeEgGaA])(.|\\n)*"
+ "(%([{](public|private)[}])?[+\\- #0]?(([0-9]+)|[\\\\*])?(\\.(([0-9]+)|[\\*]))?(hh|h|ll|l|j|z|t|L)?[oc])(.|\\n)*"
+ "(%([{](public|private)[}])?[+\\- #0]?[0-9]*(hh|h|ll|l|j|z|t)?[xXp])(.|\\n)*"
+ "(%([{](public|private)[}])?[-]@)(.|\\n)*"
+ "(%([{](public|private)[}])?l@)(.|\\n)*"
+ "(%)([+\\- #0]?[0-9]*)(hh|h|ll|l|j|z|t)?([xXp])(.|\\n)*"
+ "([^}]*)[}](.|\\n)*"
+ "([{][^{}]*[}])(.|\\n)*"
+ "(extra format specifier '"
+ "(invalid & extra format specifier: '"
+ "0x"
+ "??? (hex)"
+ "ASSERT: Invalid format specifier '%s'\n"
+ "Delete if not open returned %d (errno: %d (%{public}s), status: %{public}s) for %{public}@ "
+ "MacOS error %{public}s for %{public}@"
+ "RmDir returned %{public}s for %{public}@ "
+ "TCFURLInfo::TranslateRawPOSIXError %d (%{public}s) -> %{public}s, path: %{public}@"
+ "[{]([^{}%]*:)?([^}%]*)[%}](.|\\n)*"
+ "ll"
+ "unlink returned %d (errno: %d (%{public}s), status: %{public}s) for %{public}@ "
+ "{{"
+ "}}"
- "'null'"
- "Delete if not open retuned %d for %{public}@ "
- "EnableRedactionOnInternal"
- "MacOS error %d for %{public}@"
- "RmDir returned %d for %{public}@ "
- "TCFURLInfo::TranslateRawPOSIXError %d -> %d, path: %s"
- "unlink returned %d for %{public}@ "

```
