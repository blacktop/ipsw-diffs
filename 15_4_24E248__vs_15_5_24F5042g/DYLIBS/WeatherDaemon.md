## WeatherDaemon

> `/System/Library/PrivateFrameworks/WeatherDaemon.framework/Versions/A/WeatherDaemon`

```diff

-868.0.1.0.0
-  __TEXT.__text: 0x22e080
-  __TEXT.__auth_stubs: 0x5100
+881.0.0.0.0
+  __TEXT.__text: 0x233980
+  __TEXT.__auth_stubs: 0x51d0
   __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x11608
-  __TEXT.__cstring: 0x4497
-  __TEXT.__oslogstring: 0xa636
-  __TEXT.__constg_swiftt: 0x41c8
-  __TEXT.__swift5_typeref: 0x4c12
+  __TEXT.__const: 0x116b8
+  __TEXT.__cstring: 0x4557
+  __TEXT.__oslogstring: 0xa7d6
+  __TEXT.__constg_swiftt: 0x41e0
+  __TEXT.__swift5_typeref: 0x4d58
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x4502
-  __TEXT.__swift5_fieldmd: 0x5fd4
+  __TEXT.__swift5_reflstr: 0x4582
+  __TEXT.__swift5_fieldmd: 0x6004
   __TEXT.__swift5_types: 0x5a4
   __TEXT.__swift5_proto: 0x119c
   __TEXT.__swift5_protos: 0xb0

   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift_as_entry: 0x2e4
   __TEXT.__swift_as_ret: 0x3b4
-  __TEXT.__unwind_info: 0x7920
-  __TEXT.__eh_frame: 0xd2d0
+  __TEXT.__unwind_info: 0x7a80
+  __TEXT.__eh_frame: 0xd638
   __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0xe2a
+  __TEXT.__objc_methname: 0xe51
   __TEXT.__objc_methtype: 0x566
   __TEXT.__objc_stubs: 0x240
   __DATA_CONST.__got: 0xef8

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2888
-  __AUTH_CONST.__auth_ptr: 0x13a8
-  __AUTH_CONST.__const: 0xe310
+  __AUTH_CONST.__auth_got: 0x28f0
+  __AUTH_CONST.__auth_ptr: 0x14a0
+  __AUTH_CONST.__const: 0xe428
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x38a8
   __AUTH.__objc_data: 0x9c8
   __AUTH.__data: 0x4518
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x54a8
-  __DATA.__bss: 0x21750
+  __DATA.__data: 0x5518
+  __DATA.__bss: 0x21780
   __DATA.__common: 0x248
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12061
-  Symbols:   4874
-  CStrings:  1412
+  Functions: 12131
+  Symbols:   4932
+  CStrings:  1424
 
Symbols:
+ _symbolic Ss
+ _symbolic Ss_Ss7versionSs3latSs3lonSst
+ _symbolic Ss_Ss7versionSs8languaget
+ _symbolic _____Sg 13WeatherDaemon0A14RequestOptionsV
+ _symbolic _____Sg So22CLLocationCoordinate2DV
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _symbolic _____ySs_Ss7versionSs3latSs3lonSstG 17_StringProcessing5RegexV
+ _symbolic _____ySs_Ss7versionSs3latSs3lonSst_G 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_Ss7versionSs3latSs3lonSst_GSg 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_Ss7versionSs8languagetG 17_StringProcessing5RegexV
+ _symbolic _____ySs_Ss7versionSs8languaget_G 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_Ss7versionSs8languaget_GSg 17_StringProcessing5RegexV5MatchV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5Int64V
+ objectdestroy.38Tm
+ objectdestroy.50Tm
+ objectdestroy.62Tm
- _OBJC_CLASS_$_NSURLCache
- objectdestroy.34Tm
- objectdestroy.46Tm
- objectdestroy.58Tm
CStrings:
+ "/\\/v(?<version>\\d+)\\/weather\\/(?<language>.+?)\\//"
+ "/\\/v(?<version>\\d+)\\/weather\\/.+?\\/(?<lat>.+?)\\/(?<lon>.*?(\\/|$))/"
+ "Starting new request, cachingEnabled=%{bool}d"
+ "URLCache"
+ "configuration"
+ "dateFromString:"
+ "insertIntoCache: %{private,mask.hash}s: Could not parse request location"
+ "insertIntoCache: %{private,mask.hash}s: Could not parse request options"
+ "insertIntoCache: %{private,mask.hash}s: Could not parse request products"
+ "insertIntoCache: %{private,mask.hash}s: Inserted successfully"
+ "insertIntoCache: Could not parse request components"
+ "relativeHourlyTo"

```
