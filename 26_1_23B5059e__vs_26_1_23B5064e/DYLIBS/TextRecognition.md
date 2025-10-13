## TextRecognition

> `/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition`

```diff

-430.0.0.0.0
-  __TEXT.__text: 0x1c8e8c
+430.1.1.0.0
+  __TEXT.__text: 0x1c986c
   __TEXT.__auth_stubs: 0x3760
-  __TEXT.__objc_methlist: 0x93fc
+  __TEXT.__objc_methlist: 0x9414
   __TEXT.__const: 0x439e
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x1f7c
-  __TEXT.__cstring: 0x1c75e
+  __TEXT.__cstring: 0x1cead
   __TEXT.__swift5_capture: 0xa60
-  __TEXT.__oslogstring: 0x4f1f
+  __TEXT.__oslogstring: 0x4ef7
   __TEXT.__constg_swiftt: 0x1510
   __TEXT.__swift5_reflstr: 0xec0
   __TEXT.__swift5_fieldmd: 0xe80

   __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__gcc_except_tab: 0x14ab4
-  __TEXT.__ustring: 0xa8e0
-  __TEXT.__unwind_info: 0x7238
+  __TEXT.__gcc_except_tab: 0x14cbc
+  __TEXT.__ustring: 0xabf6
+  __TEXT.__unwind_info: 0x7258
   __TEXT.__eh_frame: 0x65a8
   __TEXT.__objc_classname: 0x1452
-  __TEXT.__objc_methname: 0x16cb7
-  __TEXT.__objc_methtype: 0x74b7
+  __TEXT.__objc_methname: 0x16d24
+  __TEXT.__objc_methtype: 0x74d8
   __TEXT.__objc_stubs: 0xed40
   __DATA_CONST.__got: 0xe98
   __DATA_CONST.__const: 0x1d10

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a90
+  __DATA_CONST.__objc_selrefs: 0x4aa0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x3b8
-  __DATA_CONST.__objc_arraydata: 0x17d00
+  __DATA_CONST.__objc_arraydata: 0x1a010
   __AUTH_CONST.__auth_got: 0x1bc8
-  __AUTH_CONST.__const: 0x4910
-  __AUTH_CONST.__cfstring: 0x2d920
+  __AUTH_CONST.__const: 0x4970
+  __AUTH_CONST.__cfstring: 0x30bc0
   __AUTH_CONST.__objc_const: 0x13cf8
   __AUTH_CONST.__objc_intobj: 0x630
-  __AUTH_CONST.__objc_arrayobj: 0x2a90
-  __AUTH_CONST.__objc_dictobj: 0x5488
-  __AUTH_CONST.__objc_doubleobj: 0xe80
+  __AUTH_CONST.__objc_arrayobj: 0x2b08
+  __AUTH_CONST.__objc_dictobj: 0x5528
+  __AUTH_CONST.__objc_doubleobj: 0xec0
   __AUTH_CONST.__objc_floatobj: 0x220
   __AUTH.__objc_data: 0xa28
   __AUTH.__data: 0x328

   __DATA_DIRTY.__objc_ivar: 0xfc
   __DATA_DIRTY.__objc_data: 0x37a0
   __DATA_DIRTY.__data: 0x1730
-  __DATA_DIRTY.__bss: 0x12a8
+  __DATA_DIRTY.__bss: 0x12d8
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A6A864ED-FE47-301B-8630-62E10889B529
-  Functions: 6910
-  Symbols:   15911
-  CStrings:  20992
+  UUID: E88ABA52-88E2-3238-B98B-A794545E138F
+  Functions: 6915
+  Symbols:   15927
+  CStrings:  21674
 
Symbols:
+ +[CRLineWrappingClassifier modelLocaleForExtendedLatin]
+ +[CRWrappingClassifierFeatureExtractor _extractLocaleFeaturesTo:locale:]
+ +[CRWrappingClassifierFeatureExtractor evaluationResultForTextFeature:withLastFeature:locale:imageSize:]
+ -[CRLineWrappingContext classifierShouldInsertLineBreakForEvaluationResult:threshold:useThresholdOverride:]
+ _OBJC_CLASS_$_NLLanguageRecognizer
+ ___49+[CRLineWrappingClassifier modelLocaleForLocale:]_block_invoke
+ ___54-[CRLineWrappingContext _probabilityThresholdOverride]_block_invoke
+ ___72+[CRWrappingClassifierFeatureExtractor _extractLocaleFeaturesTo:locale:]_block_invoke
+ ___block_literal_global.199
+ _objc_msgSend$_extractLocaleFeaturesTo:locale:
+ _objc_msgSend$classifierShouldInsertLineBreakForEvaluationResult:threshold:useThresholdOverride:
+ _objc_msgSend$modelLocaleForExtendedLatin
- +[CRLineWrappingClassifier _lineWrappingShouldFallBackForLocale:]
- -[CRLineWrappingContext classifierShouldInsertLineBreakForEvaluationResult:threshold:]
- _OBJC_CLASS_$_NLCFROLanguageRecognizer
- _objc_msgSend$_lineWrappingShouldFallBackForLocale:
- _objc_msgSend$classifierShouldInsertLineBreakForEvaluationResult:threshold:
- _objc_msgSend$languageIsNorwegian:
CStrings:
+ "\x05&"
+ "\r\x01e"
+ "\x12 "
+ "\x12\""
+ "\x13 "
+ "\x13'"
+ "\x14 "
+ "\x14'"
+ "\x17\""
+ "\x18\""
+ "\x19\x02i"
+ "#%lu/%lu wrap=%lu (unchanged): |%{sensitive}@|%{sensitive}@| (%@)"
+ "#%lu/%lu wrap=%lu: |%{sensitive}@|%{sensitive}@| (%@) reason=%@"
+ "%s: Unexpected nil context"
+ "-[CRWrappingEvaluationResult _computeGeometricProperties]"
+ "-[CRWrappingEvaluationResult _computeLMScoreComputingEOS:]"
+ "-[CRWrappingEvaluationResult caseWrappingScoreUsingCustomConfiguration:]"
+ "-[CRWrappingEvaluationResult excessiveVerticalDistance]"
+ "-[CRWrappingEvaluationResult featureTokens]"
+ "-[CRWrappingEvaluationResult punctuationWrappingScoreUsingCustomConfiguration:]"
+ "-[CRWrappingEvaluationResult wordCountWrappingScore]"
+ "1)"
+ "1x"
+ "2)"
+ "3'"
+ "3)"
+ "4)"
+ "5)"
+ "7)"
+ "=\xd8\xce\xdf"
+ "=\xd8\xf8\xdd"
+ "@56@0:8@16@24@32{CGSize=dd}40"
+ "B\x01y"
+ "B32@0:8@16f24B28"
+ "Failed to load line wrapping config for locale %s and category %s"
+ "NIL"
+ "_extractLocaleFeaturesTo:locale:"
+ "`$"
+ "a$"
+ "a&"
+ "a)"
+ "aby"
+ "acum"
+ "adalah"
+ "af"
+ "akan"
+ "aku"
+ "ale"
+ "allergener:"
+ "alt"
+ "apabila"
+ "asi"
+ "atau"
+ "att"
+ "av"
+ "ayam"
+ "b$"
+ "b)"
+ "bagi"
+ "bakar"
+ "bakso"
+ "bawang"
+ "bayaran"
+ "biji"
+ "bisa"
+ "blir"
+ "blive"
+ "bliver"
+ "boleh"
+ "buah"
+ "buc"
+ "buc."
+ "byla"
+ "bylo"
+ "c$"
+ "c)"
+ "c.i.f."
+ "cafea"
+ "cara"
+ "cartofi"
+ "cate"
+ "cawan"
+ "ceai"
+ "cele"
+ "cena"
+ "ciebie"
+ "cili"
+ "classifierShouldInsertLineBreakForEvaluationResult:threshold:useThresholdOverride:"
+ "cod"
+ "coklat"
+ "contoh"
+ "contoh:"
+ "cr_lw_extlatin.mlmodelc"
+ "cu"
+ "cukru"
+ "cum"
+ "czy"
+ "d)"
+ "daging"
+ "dalam"
+ "dan"
+ "dapat"
+ "dar"
+ "deg"
+ "dengan"
+ "det"
+ "dette"
+ "dig"
+ "dkk"
+ "dl"
+ "dla"
+ "dosen"
+ "drogi"
+ "e&"
+ "ei"
+ "eller"
+ "ett"
+ "evaluationResultForTextFeature:withLastFeature:locale:imageSize:"
+ "extlatin"
+ "favorit!"
+ "fett"
+ "fettsyrer"
+ "fi"
+ "foarte"
+ "fordi"
+ "fost"
+ "fra"
+ "garam"
+ "goreng"
+ "gr"
+ "gula"
+ "hadde"
+ "hans"
+ "hanya"
+ "har"
+ "harga"
+ "havde"
+ "helt"
+ "hitam"
+ "hun"
+ "hvis"
+ "hvor"
+ "hvorav"
+ "hvordan"
+ "iar"
+ "ikan"
+ "ikke"
+ "ikkje"
+ "ingin"
+ "ingredienser:"
+ "ingrediente"
+ "ingrediente:"
+ "ini"
+ "ini."
+ "inkluderet"
+ "inneholder:"
+ "isi"
+ "jag"
+ "jak"
+ "jako"
+ "jangan"
+ "jeg"
+ "jehlany"
+ "jeruk"
+ "jest"
+ "jestem"
+ "jika"
+ "jsem"
+ "jsme"
+ "juga"
+ "jumlah"
+ "jus"
+ "kamu"
+ "kan"
+ "karena"
+ "kawa"
+ "keju"
+ "kek"
+ "kerana"
+ "kita"
+ "kom"
+ "kopi"
+ "kotlet"
+ "kr"
+ "kr."
+ "kunne"
+ "kyckling"
+ "lapis"
+ "linguri"
+ "localeMismatch:%@:%@"
+ "lui"
+ "malaysia"
+ "mam"
+ "mange"
+ "manis"
+ "maret"
+ "masak"
+ "med"
+ "meg"
+ "meget"
+ "memberikan"
+ "men"
+ "menggunakan"
+ "meniu"
+ "menjadi"
+ "menu"
+ "merah"
+ "mig"
+ "mine"
+ "minuman"
+ "mnie"
+ "moc"
+ "modelLocaleForExtendedLatin"
+ "mult"
+ "nama"
+ "nasi"
+ "nebo"
+ "och"
+ "og"
+ "onsdag"
+ "oraz"
+ "oslo"
+ "paa"
+ "pada"
+ "pagi"
+ "pak"
+ "peber"
+ "pendapatan"
+ "pentru"
+ "pesan"
+ "pierogi"
+ "pln"
+ "po-"
+ "poate"
+ "praha"
+ "prin"
+ "pro-"
+ "proteine"
+ "przez"
+ "pui"
+ "putih"
+ "ribu"
+ "rigtig"
+ "rm"
+ "ron"
+ "roti"
+ "rp"
+ "rp."
+ "saa"
+ "sangat"
+ "sare"
+ "saya"
+ "schabowy"
+ "sdm"
+ "sdt"
+ "sebagai"
+ "sebanyak"
+ "seg"
+ "selalu"
+ "selamat"
+ "semoga"
+ "seria:"
+ "serta"
+ "sig"
+ "skal"
+ "skulle"
+ "som"
+ "soto"
+ "srl"
+ "ss"
+ "stk"
+ "styrka"
+ "sunt"
+ "susu"
+ "tam"
+ "tapi"
+ "tarikh"
+ "teh"
+ "telah"
+ "telur"
+ "tepung"
+ "tetapi"
+ "textEvaluationWithoutNewColumn:%ld"
+ "tidak"
+ "til"
+ "till"
+ "to,"
+ "toko"
+ "torsdag"
+ "trebuie"
+ "tva"
+ "twoje"
+ "ul."
+ "unei"
+ "unitatea:"
+ "untuk"
+ "useLocaleTokens"
+ "valoare"
+ "var"
+ "vechi:"
+ "ved"
+ "verde"
+ "vil"
+ "wang"
+ "warszawa"
+ "za-"
+ "zapraszamy"
+ "zl"
+ "zupa"
+ "|\x01e"
+ "~\x01e"
+ "\x81)"
+ "\x92!"
+ "\xa0%"
+ "\xa1%"
+ "\xaa%"
+ "\xac&"
+ "\xae%"
+ "\xb3!"
+ "\xb7"
+ "\xb7%"
+ "\xb9&"
+ "\xbd"
+ "\xcb%"
+ "\xd2!"
+ "\xe4"
+ "\xe5"
+ "\xe6"
+ "\xe6%"
+ "\xee"
+ "\xf6'"
- "%s: Line %lu/%lu - Keeping lineWrappingType %lu: '%{sensitive}@' | '%{sensitive}@'."
- "%s: Line %lu/%lu - Updating lineWrappingType %lu: '%{sensitive}@' | '%{sensitive}@' (%@)."
- "-[CRLineWrapper predictLineWrappingTypesForAllLinesInGroups:useHandwritingConfig:]"
- "B28@0:8@16f24"
- "Failed to load line wrapping config for locale %%@ and category %s"
- "Unexpected nil context"
- "_lineWrappingShouldFallBackForLocale:"
- "classifierShouldInsertLineBreakForEvaluationResult:threshold:"
- "localeMismatch"
- "textEvaluationWithoutNewColumn"

```
