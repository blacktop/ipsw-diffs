## iPodVoiceOver

> `/System/Library/PrivateFrameworks/iPodVoiceOver.framework/Versions/A/iPodVoiceOver`

```diff

-  __TEXT.__text: 0x100c40
+  __TEXT.__text: 0x100874
   __TEXT.__objc_methlist: 0x170
   __TEXT.__cstring: 0x10a4b
   __TEXT.__const: 0x3fd40
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__speechdata: 0x2022f95
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x1930
+  __TEXT.__unwind_info: 0x1928
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _LanguageIdentifierLoadModel : 556 -> 540
~ _LanguageIdentifierDecideLanguage : 2228 -> 2224
~ _SetVoiceVersion : 212 -> 228
~ _GetVoiceVersion : 132 -> 136
~ _GetVoiceForLanguage : 120 -> 124
~ _TtsCreateInstance : 1196 -> 1204
~ _vplatform_datastream_Open : 540 -> 516
~ _txtwriter_ClassOpen : 1392 -> 1380
~ _pcre_compile : 5736 -> 5732
~ _check_escape : 728 -> 700
~ _compile_regex : 13548 -> 13332
~ _pcre_exec2 : 2020 -> 1996
~ _match : 26340 -> 26028
~ _find_fixedlength : 616 -> 608
~ _could_be_empty_branch : 732 -> 728
~ _LH_wcscat_from_char : 40 -> 44
~ _LH_wcsncpy_to_char : 112 -> 100
~ _LH_wcslen : 32 -> 28
~ _LH_wcsncpy : 128 -> 116
~ _LH_itoa : 156 -> 148
~ _LH_utoa : 124 -> 116
~ _LH_wcstoxl : 576 -> 584
~ _hdrpars_ReadHeader : 1416 -> 1408
~ _hdrpars_ParseElement : 2164 -> 2072
~ _hdrpars_ParseAttributes : 728 -> 708
~ _brkhlp_GetBuiltinInterface : 160 -> 168
~ _chars_ScanBlankHead : 336 -> 308
~ _utoin_IncrReplaceCurrentRegion : 612 -> 628
~ _utoin_MarkSingleLatinForSpell : 916 -> 944
~ _getUTOIMarkerString : 88 -> 96
~ _mbs_normalize : 620 -> 644
~ _mDictFind : 120 -> 124
~ _o2t_Transcribe : 1176 -> 1180
~ _SParser : 10112 -> 10124
~ _compareXX : 916 -> 932
~ _rule2phone : 3376 -> 3384
~ _sparser_SetReadoutMarkersAsParameters : 1456 -> 1476
~ _escseqm_str2enumMapping : 284 -> 300
~ _escseqm_get_token : 2972 -> 2988
~ _escseqm_GetDefaults : 424 -> 432
~ _utois_ScanRegions : 5776 -> 5836
~ _escseqs_Process : 4672 -> 4616
~ _seq_WriteTextAndMarkers1 : 5500 -> 5524
~ _fe_pos_Process : 4884 -> 4820
~ _abbrtn_Lookup : 4972 -> 4952
~ _fe_ara_parser_Process : 4808 -> 4788
~ _araParser_markWords : 1288 -> 1308
~ _araParser_NormalizeSentence : 616 -> 620
~ _araParser_doNGramProcessing : 5016 -> 5028
~ _CLM_FindNrOfLanguages : 496 -> 504
~ _fe_puncsptn_Process : 10140 -> 10080
~ _EXEC_RULE : 5208 -> 5160
~ _hlp_Phrasing : 3164 -> 3148
~ _fe_global_Process : 10248 -> 10232
~ _activeprompt_db_Get : 392 -> 400
~ _hlp_GetMimeParam : 344 -> 356
~ _LhplGetSymbol : 4144 -> 4208
~ _VP_Calc_R_and_r_LF0_MU : 492 -> 496
~ _VP_Calc_R_and_r_MCP_MU : 460 -> 468
~ _mlpg_MCP_cv_fx : 560 -> 564
~ _InitTempVarPStream : 600 -> 592
~ _AddInputMatricesTempVarPStream : 400 -> 392
~ _InitPStream : 364 -> 360
~ _zerflt_qs : 88 -> 80
~ _MFVSyn__mlsa_filter_mlp_fill : 348 -> 316
~ _MFVSyn__mlsa_filter : 2488 -> 2396
~ _ruleset_ReadRules : 1748 -> 1720
~ _ruleset_IsSectionHeader : 304 -> 316
~ _ruleset_ReadLine : 664 -> 640
~ _audioins_Process : 1904 -> 1912
~ _audiofetch_FetchStreamOpen : 816 -> 824
~ _ucs2_utf8_byte_count : 112 -> 128
~ _edct_GetEntryDataSpec_In_RWDCT : 444 -> 432
~ _edct_GetEntryDataSpec_In_RODCT : 444 -> 432
~ _lhstdlib_qsort : 988 -> 940
~ _lhstdlib_udqsort : 1028 -> 972
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HhT8lg/Sources/iPodVoiceOver/Shared/LangId/Viterbi/LanguageIdentification.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HhT8lg/Sources/iPodVoiceOver/Shared/LibrarySource/VoSession.c"
+ "01:56:48"
+ "Jun 23 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7zznTO/Sources/iPodVoiceOver/Shared/LangId/Viterbi/LanguageIdentification.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7zznTO/Sources/iPodVoiceOver/Shared/LibrarySource/VoSession.c"
- "07:06:10"
- "Jun  9 2026"

```
