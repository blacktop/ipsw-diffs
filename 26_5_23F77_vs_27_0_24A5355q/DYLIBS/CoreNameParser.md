## CoreNameParser

> `/System/Library/PrivateFrameworks/CoreNameParser.framework/CoreNameParser`

```diff

 14.0.0.0.0
-  __TEXT.__text: 0x60ec
-  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__text: 0x5dcc
   __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x397
+  __TEXT.__cstring: 0x39f
   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__ustring: 0x3c
-  __TEXT.__unwind_info: 0x1d8
-  __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x10cd
-  __TEXT.__objc_methtype: 0x2a1
-  __TEXT.__objc_stubs: 0x1260
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0x620
   __AUTH_CONST.__objc_const: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x1f0
   __DATA.__objc_ivar: 0x44
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E791A936-E875-3BD5-82E4-D6F8BE4B173C
+  UUID: 9AE8A292-3EB7-345F-A0C5-5868960C313F
   Functions: 123
-  Symbols:   570
-  CStrings:  332
+  Symbols:   571
+  CStrings:  103
 
Symbols:
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.115
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x3
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.116
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
- ".cxx_destruct"
- "@\"NPHMMClassifier\""
- "@\"NPNameComponentsData\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@32@0:8@16^d24"
- "@32@0:8Q16Q24"
- "@36@0:8@16B24^d28"
- "@40@0:8@16@24Q32"
- "@48@0:8Q16Q24@32@40"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32d40d48d56"
- "@80@0:8{?={?=ddd}{?=ddd}d}16@72"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8Q16@24"
- "B40@0:8@16@24@32"
- "NPComponentSequence"
- "NPHMMClassifier"
- "NPNameComponentsData"
- "NPNameParser"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q32@0:8@16Q24"
- "T@\"NPHMMClassifier\",&,V_classifier"
- "T@\"NSArray\",C,V_observation"
- "T@\"NSArray\",C,V_oovIndices"
- "T@\"NSArray\",C,V_sequence"
- "TB,GisFavorite,V_favorite"
- "Td,V_emissionModelScore"
- "Td,V_score"
- "Td,V_stateModelScore"
- "T{?={?=ddd}{?=ddd}d},V_stateProbabilities"
- "^{_CFBurstTrie=}16@0:8"
- "_classifier"
- "_confidenceThreshold"
- "_emissionModelScore"
- "_favorite"
- "_keyForDataEntry:"
- "_nameComponents"
- "_nameComponentsData"
- "_observation"
- "_oovIndices"
- "_score"
- "_sequence"
- "_stateModelScore"
- "_stateProbabilities"
- "_totalFamilyNamesCount"
- "_totalGivenNamesCount"
- "_uniqueFamilyNamesCount"
- "_uniqueGivenNamesCount"
- "addCharactersInRange:"
- "addObject:"
- "allKeys"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "boolValue"
- "bundleForClass:"
- "candidatesBasedOnCommaDelimiterIndex:sequenceSize:"
- "candidatesBasedOnFormatSequence:"
- "candidatesOfSize:constraints:compoundsConstraints:labelsContraints:"
- "caseInsensitiveCompare:"
- "characterAtIndex:"
- "characterIsMember:"
- "characterSetWithCharactersInString:"
- "classifier"
- "collectionForEntry:contains:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "compoundsFromName:"
- "compoundsFromName:includeSpaceAsDelimiter:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "currentLocale"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d32@0:8@16@24"
- "d40@0:8@16Q24^B32"
- "dealloc"
- "description"
- "doubleValue"
- "emissionModelScore"
- "emissionProbability:hiddenState:isOOV:"
- "enumerateLinguisticTagsInRange:scheme:options:orthography:usingBlock:"
- "extractMetricForType:"
- "familyName"
- "favorite"
- "filteredArrayUsingPredicate:"
- "firstObject"
- "formCompoundFamilyName:"
- "formCompoundGivenName:"
- "frequencyForName:type:"
- "frequencyOfLatinFamilyName:"
- "frequencyOfLatinGivenName:"
- "genderMajorityForGivenName:"
- "givenName"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasPrefix:"
- "hiddenStatesFromObservationSequence:"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "init"
- "initWithCapacity:"
- "initWithCharacters:length:"
- "initWithContentsOfFile:options:error:"
- "initWithDominantScript:languageMap:"
- "initWithHMMProbabilities:nameComponentsDate:"
- "initWithObservationSequence:hiddenSequence:oovIndices:emissionModelScore:stateModelScore:boost:"
- "integerValue"
- "invertedSet"
- "isCoupleName:"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToComponentSequence:"
- "isEqualToString:"
- "isFavorite"
- "isGivenNameAbbreviation:"
- "isInitial:"
- "isLinkingToken:"
- "isParticle:"
- "isPrefix:"
- "isSuffix:"
- "lastObject"
- "length"
- "letterCharacterSet"
- "lowercaseString"
- "mutableCopy"
- "nameFrequencyTrieRef"
- "namingTraditionForName:"
- "newlineCharacterSet"
- "normalizeFullname:"
- "normalizedAffix:"
- "numberOfMatchesInString:options:range:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectValueForEntry:"
- "observation"
- "oovIndices"
- "oovTokens"
- "parseChineseName:"
- "parseChineseName:normalize:"
- "parseFullnameWithDefaultHMMClassifier:"
- "parseFullnameWithDefaultHMMClassifier:normalize:score:"
- "parseJapaneseName:"
- "parseJapaneseName:normalize:"
- "parseKoreanName:"
- "parseKoreanName:normalize:"
- "parseLatinName:score:"
- "pathForResource:ofType:"
- "payloadForName:type:"
- "personNameCompomentsFromPrefix:suffix:givenNames:middleNames:familyNames:"
- "personNameComponentsFromString:"
- "predicateWithFormat:"
- "preferredLanguages"
- "probabilityForHiddenSequence:knowingObservationSequence:boost:"
- "propertyListWithData:options:format:error:"
- "rangeValue"
- "regionCode"
- "regularExpressionWithPattern:options:error:"
- "removeLastObject"
- "removeObjectAtIndex:"
- "replaceCharactersInRange:withString:"
- "reverseObjectEnumerator"
- "score"
- "sequence"
- "setClassifier:"
- "setCountLimit:"
- "setEmissionModelScore:"
- "setFamilyName:"
- "setFavorite:"
- "setGivenName:"
- "setMiddleName:"
- "setNamePrefix:"
- "setNameSuffix:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObservation:"
- "setOovIndices:"
- "setScore:"
- "setSequence:"
- "setStateModelScore:"
- "setStateProbabilities:"
- "setValue:atSequenceIndex:"
- "sharedNameFrequencyTrieRef"
- "startProbability:"
- "stateModelScore"
- "stateProbabilities"
- "stateTransitionProbabilityFrom:to:"
- "stringByAppendingString:"
- "stringByApplyingTransform:reverse:"
- "stringByReplacingMatchesInString:options:range:withTemplate:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringValue"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "unionSet:"
- "unsignedIntegerValue"
- "uppercaseString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v32@0:8@16Q24"
- "v72@0:8{?={?=ddd}{?=ddd}d}16"
- "validSequence:compoundsConstraints:labelsConstraints:"
- "valueWithRange:"
- "whitespaceAndNewlineCharacterSet"
- "{?=\"givenName\"{?=\"givenName\"d\"familyName\"d\"initial\"d}\"familyName\"{?=\"givenName\"d\"familyName\"d\"initial\"d}\"threshold\"d}"
- "{?={?=ddd}{?=ddd}d}16@0:8"

```
