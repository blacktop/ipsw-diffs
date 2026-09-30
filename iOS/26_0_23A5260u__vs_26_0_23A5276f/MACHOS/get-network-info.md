## get-network-info

> `/System/Library/Frameworks/SystemConfiguration.framework/get-network-info`

```diff

-1385.0.0.0.0
-  __TEXT.__text: 0xa3a8
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__const: 0x67c
-  __TEXT.__cstring: 0x1bf5
+1385.0.4.0.0
+  __TEXT.__text: 0xc108
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__const: 0x6ac
+  __TEXT.__cstring: 0x1b55
   __TEXT.__constg_swiftt: 0x190
-  __TEXT.__swift5_typeref: 0x1e9
+  __TEXT.__swift5_typeref: 0x26d
   __TEXT.__swift5_reflstr: 0x2b3
   __TEXT.__swift5_fieldmd: 0x1d8
-  __TEXT.__objc_methname: 0x170
+  __TEXT.__objc_methname: 0x18d
   __TEXT.__oslogstring: 0x3
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__eh_frame: 0x178
-  __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x228
-  __DATA_CONST.__const: 0xf80
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__eh_frame: 0x220
+  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0x240
+  __DATA_CONST.__const: 0xf60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x330
-  __DATA.__objc_selrefs: 0x88
+  __DATA.__objc_selrefs: 0x90
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x550
-  __DATA.__bss: 0xa80
+  __DATA.__data: 0x5d8
+  __DATA.__bss: 0xa90
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5508B5B7-495C-3B52-9169-8C5F47A05A09
-  Functions: 160
-  Symbols:   294
-  CStrings:  195
+  UUID: 13151AE7-B8D7-31FA-A059-E3B61EA8643C
+  Functions: 167
+  Symbols:   316
+  CStrings:  198
 
Symbols:
+ _$s10Foundation12CharacterSetV8newlinesACvgZ
+ _$s12RegexBuilder0a9ComponentB0O15buildExpressionyxx17_StringProcessing0aC0RzlFZ
+ _$s12RegexBuilder0a9ComponentB0O17buildPartialBlock5first17_StringProcessing0A0Vy0A6OutputQzGx_tAF0aC0RzlFZ
+ _$s12RegexBuilder11makeFactory17_StringProcessing01_aD0VyF
+ _$s12RegexBuilder7CaptureVMn
+ _$s12RegexBuilder7CaptureVyACyxG17_StringProcessing0A0VyxGcfC
+ _$s12RegexBuilder7CaptureVyxG17_StringProcessing0A9ComponentAAMc
+ _$s17_StringProcessing13_RegexFactoryV10accumulateyAA0C0VyxGq__q0_tAA0C9ComponentR_AaHR0_r1_lF
+ _$s17_StringProcessing13_RegexFactoryV7captureyAA0C0VyxGq_AA0C9ComponentR_r0_lF
+ _$s17_StringProcessing13_RegexFactoryVMa
+ _$s17_StringProcessing14RegexComponentP5regexAA0C0Vy0C6OutputQzGvgTj
+ _$s17_StringProcessing5RegexV06_regexA07versionACyxGSS_SitcfC
+ _$s17_StringProcessing5RegexV0C7BuilderEyACyxGqd__yXEc0C6OutputQyd__RszAA0C9ComponentRd__lufC
+ _$s17_StringProcessing5RegexV10wholeMatch2inAC0E0Vyx_GSgSs_tKF
+ _$s17_StringProcessing5RegexV11prefixMatch2inAC0E0Vyx_GSgSs_tKF
+ _$s17_StringProcessing5RegexV5MatchV13dynamicMemberqd__s7KeyPathCyxqd__G_tcluig
+ _$s17_StringProcessing5RegexV5MatchVMn
+ _$s17_StringProcessing5RegexVMn
+ _$s17_StringProcessing5RegexVyxGAA0C9ComponentAAMc
+ _$sSS10FoundationE14contentsOfFile8encodingS2Sh_SSAAE8EncodingVtKcfC
+ _$sSS14_fromSubstringySSSshFZ
+ _$sSSySsSnySS5IndexVGcig
+ _$sSayxGSKsMc
+ _$sSsN
+ _objc_retain_x23
+ _swift_getKeyPath
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "#\n# cat /var/run/racoon/*.conf\n#\n"
+ "/\"?([^\\s;\"]+)\"?/"
+ "/\\s+[AE]:\\s+\\S+\\s+/"
+ "/\\s+shared_secret\\s+use\\s+/"
+ "fileHandleForUpdatingAtPath:"
+ "tmp-redaction-stdin.txt"
- "/usr/bin/perl -l -n -e '\nif (/^(\\s+[AE]:\\s+\\S+\\s+)\"?(.*)\"?\\s*$/) {\n printf \"%s[redacted]%s\\n\", $1, $3;\n} else {\n printf \"%s\\n\", $_;\n}\n'"
- "/usr/bin/perl -l -n -e '\nif (/^(\\s+shared_secret\\s+use\\s+)\"?([^\\s;\"]+)\"?(.*)/) {\n printf \"%s[redacted]%s\\n\", $1, $3;\n} else {\n printf \"%s\\n\", $_;\n}\n'"
- "tmp-perl-stdin.txt"

```
