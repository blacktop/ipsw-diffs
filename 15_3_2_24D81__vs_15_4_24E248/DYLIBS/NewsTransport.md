## NewsTransport

> `/System/Library/PrivateFrameworks/NewsTransport.framework/Versions/A/NewsTransport`

```diff

-5626.0.0.0.0
-  __TEXT.__text: 0x23c4dc
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x3404c
+5676.0.3.0.0
+  __TEXT.__text: 0x25a900
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x376ac
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x1156a
-  __TEXT.__unwind_info: 0x4bf0
-  __TEXT.__objc_classname: 0x232e
-  __TEXT.__objc_methname: 0x51d74
-  __TEXT.__objc_methtype: 0xc5a6
-  __TEXT.__objc_stubs: 0x8540
-  __DATA_CONST.__got: 0x858
-  __DATA_CONST.__const: 0x7170
-  __DATA_CONST.__objc_classlist: 0xa48
+  __TEXT.__cstring: 0x11d1d
+  __TEXT.__unwind_info: 0x5090
+  __TEXT.__objc_classname: 0x26b8
+  __TEXT.__objc_methname: 0x5588b
+  __TEXT.__objc_methtype: 0xcb73
+  __TEXT.__objc_stubs: 0x90c0
+  __DATA_CONST.__got: 0x960
+  __DATA_CONST.__const: 0x72c8
+  __DATA_CONST.__objc_classlist: 0xb88
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x106b0
-  __DATA_CONST.__objc_superrefs: 0xa48
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__cfstring: 0x150c0
-  __AUTH_CONST.__objc_const: 0x48a70
-  __AUTH.__objc_data: 0x55f0
-  __DATA.__objc_ivar: 0x3cac
+  __DATA_CONST.__objc_selrefs: 0x11520
+  __DATA_CONST.__objc_superrefs: 0xb88
+  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__cfstring: 0x15fe0
+  __AUTH_CONST.__objc_const: 0x4d7a0
+  __AUTH.__objc_data: 0x6270
+  __DATA.__objc_ivar: 0x3ffc
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x10e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7DE96FE1-3E51-3302-8C0A-991EBB77DFC2
-  Functions: 17877
-  Symbols:   25488
-  CStrings:  18832
+  UUID: 64EB3EC1-8193-3A58-BD5A-38969D7F5470
+  Functions: 18917
+  Symbols:   27276
+  CStrings:  19862
 
Symbols:
+ +[NTPBArticleRecord recipeIDsType]
+ +[NTPBCKConfiguration fieldsType]
+ +[NTPBCKConfigurationFieldValue fieldValuesType]
+ +[NTPBCKConfigurationFieldValue listValuesType]
+ +[NTPBCKLocale enabledKeyboardsType]
+ +[NTPBCKQuery filtersType]
+ +[NTPBCKQuery sortsType]
+ +[NTPBCKQuery typesType]
+ +[NTPBCKQueryRetrieveResponse queryResultsType]
+ +[NTPBCKRecord fieldsType]
+ +[NTPBCKRecordFieldValue listValueType]
+ +[NTPBCKRequestedFields fieldsType]
+ +[NTPBFetchRecordSpec desiredFieldsType]
+ +[NTPBFetchRecordSpec linkedFieldsType]
+ +[NTPBNetworkEvent smarterFetchSourcesType]
+ +[NTPBRecipeListRecord recipeIDsType]
+ +[NTPBRecipeRecord allowedStorefrontIDsType]
+ +[NTPBRecipeRecord articleIDsType]
+ +[NTPBRecipeRecord authorsType]
+ +[NTPBRecipeRecord blockedStorefrontIDsType]
+ +[NTPBRecipeRecord iAdCategoriesType]
+ +[NTPBRecipeRecord iAdKeywordsType]
+ +[NTPBRecipeRecord iAdSectionTagIDsType]
+ +[NTPBRecipeRecord topicTagIDsType]
+ +[NTPBRecipeRecord topicsType]
+ +[NTPBSmarterFetchRequest tagsFollowedType]
+ +[NTPBSmarterFetchRequest todayFeedPoolRequestsType]
+ +[NTPBSmarterFetchResponse todayFeedPoolResponseType]
+ +[NTPBTodayFeedPoolRequest fetchRecordSpecsType]
+ +[NTPBTodayFeedPoolResponse recordsType]
+ +[NTPBUserInfo preferredLanguagesType]
+ -[NTPBArticleRecord addRecipeIDs:]
+ -[NTPBArticleRecord clearRecipeIDs]
+ -[NTPBArticleRecord recipeIDsAtIndex:]
+ -[NTPBArticleRecord recipeIDsCount]
+ -[NTPBArticleRecord recipeIDs]
+ -[NTPBArticleRecord setRecipeIDs:]
+ -[NTPBArticleTopic hasIsEligibleForFoodGroupingIfAutofavorited]
+ -[NTPBArticleTopic hasIsEligibleForFoodGroupingIfFavorited]
+ -[NTPBArticleTopic hasIsEligibleForFoodGrouping]
+ -[NTPBArticleTopic isEligibleForFoodGroupingIfAutofavorited]
+ -[NTPBArticleTopic isEligibleForFoodGroupingIfFavorited]
+ -[NTPBArticleTopic isEligibleForFoodGrouping]
+ -[NTPBArticleTopic setHasIsEligibleForFoodGrouping:]
+ -[NTPBArticleTopic setHasIsEligibleForFoodGroupingIfAutofavorited:]
+ -[NTPBArticleTopic setHasIsEligibleForFoodGroupingIfFavorited:]
+ -[NTPBArticleTopic setIsEligibleForFoodGrouping:]
+ -[NTPBArticleTopic setIsEligibleForFoodGroupingIfAutofavorited:]
+ -[NTPBArticleTopic setIsEligibleForFoodGroupingIfFavorited:]
+ -[NTPBCKConfiguration .cxx_destruct]
+ -[NTPBCKConfiguration addFields:]
+ -[NTPBCKConfiguration clearFields]
+ -[NTPBCKConfiguration copyWithZone:]
+ -[NTPBCKConfiguration created]
+ -[NTPBCKConfiguration description]
+ -[NTPBCKConfiguration dictionaryRepresentation]
+ -[NTPBCKConfiguration expires]
+ -[NTPBCKConfiguration fieldsAtIndex:]
+ -[NTPBCKConfiguration fieldsCount]
+ -[NTPBCKConfiguration fields]
+ -[NTPBCKConfiguration hasCreated]
+ -[NTPBCKConfiguration hasExpires]
+ -[NTPBCKConfiguration hash]
+ -[NTPBCKConfiguration isEqual:]
+ -[NTPBCKConfiguration mergeFrom:]
+ -[NTPBCKConfiguration readFrom:]
+ -[NTPBCKConfiguration setCreated:]
+ -[NTPBCKConfiguration setExpires:]
+ -[NTPBCKConfiguration setFields:]
+ -[NTPBCKConfiguration setHasCreated:]
+ -[NTPBCKConfiguration setHasExpires:]
+ -[NTPBCKConfiguration writeTo:]
+ -[NTPBCKConfigurationField .cxx_destruct]
+ -[NTPBCKConfigurationField copyWithZone:]
+ -[NTPBCKConfigurationField description]
+ -[NTPBCKConfigurationField dictionaryRepresentation]
+ -[NTPBCKConfigurationField hasName]
+ -[NTPBCKConfigurationField hasValue]
+ -[NTPBCKConfigurationField hash]
+ -[NTPBCKConfigurationField isEqual:]
+ -[NTPBCKConfigurationField mergeFrom:]
+ -[NTPBCKConfigurationField name]
+ -[NTPBCKConfigurationField readFrom:]
+ -[NTPBCKConfigurationField setName:]
+ -[NTPBCKConfigurationField setValue:]
+ -[NTPBCKConfigurationField value]
+ -[NTPBCKConfigurationField writeTo:]
+ -[NTPBCKConfigurationFieldValue .cxx_destruct]
+ -[NTPBCKConfigurationFieldValue addFieldValues:]
+ -[NTPBCKConfigurationFieldValue addListValues:]
+ -[NTPBCKConfigurationFieldValue boolValue]
+ -[NTPBCKConfigurationFieldValue bytesValue]
+ -[NTPBCKConfigurationFieldValue clearFieldValues]
+ -[NTPBCKConfigurationFieldValue clearListValues]
+ -[NTPBCKConfigurationFieldValue copyWithZone:]
+ -[NTPBCKConfigurationFieldValue description]
+ -[NTPBCKConfigurationFieldValue dictionaryRepresentation]
+ -[NTPBCKConfigurationFieldValue doubleValue]
+ -[NTPBCKConfigurationFieldValue fieldValuesAtIndex:]
+ -[NTPBCKConfigurationFieldValue fieldValuesCount]
+ -[NTPBCKConfigurationFieldValue fieldValues]
+ -[NTPBCKConfigurationFieldValue hasBoolValue]
+ -[NTPBCKConfigurationFieldValue hasBytesValue]
+ -[NTPBCKConfigurationFieldValue hasDoubleValue]
+ -[NTPBCKConfigurationFieldValue hasLongValue]
+ -[NTPBCKConfigurationFieldValue hasStringValue]
+ -[NTPBCKConfigurationFieldValue hasType]
+ -[NTPBCKConfigurationFieldValue hash]
+ -[NTPBCKConfigurationFieldValue isEqual:]
+ -[NTPBCKConfigurationFieldValue listValuesAtIndex:]
+ -[NTPBCKConfigurationFieldValue listValuesCount]
+ -[NTPBCKConfigurationFieldValue listValues]
+ -[NTPBCKConfigurationFieldValue longValue]
+ -[NTPBCKConfigurationFieldValue mergeFrom:]
+ -[NTPBCKConfigurationFieldValue readFrom:]
+ -[NTPBCKConfigurationFieldValue setBoolValue:]
+ -[NTPBCKConfigurationFieldValue setBytesValue:]
+ -[NTPBCKConfigurationFieldValue setDoubleValue:]
+ -[NTPBCKConfigurationFieldValue setFieldValues:]
+ -[NTPBCKConfigurationFieldValue setHasBoolValue:]
+ -[NTPBCKConfigurationFieldValue setHasDoubleValue:]
+ -[NTPBCKConfigurationFieldValue setHasLongValue:]
+ -[NTPBCKConfigurationFieldValue setHasType:]
+ -[NTPBCKConfigurationFieldValue setListValues:]
+ -[NTPBCKConfigurationFieldValue setLongValue:]
+ -[NTPBCKConfigurationFieldValue setStringValue:]
+ -[NTPBCKConfigurationFieldValue setType:]
+ -[NTPBCKConfigurationFieldValue stringValue]
+ -[NTPBCKConfigurationFieldValue type]
+ -[NTPBCKConfigurationFieldValue writeTo:]
+ -[NTPBCKDate copyWithZone:]
+ -[NTPBCKDate description]
+ -[NTPBCKDate dictionaryRepresentation]
+ -[NTPBCKDate hasTime]
+ -[NTPBCKDate hash]
+ -[NTPBCKDate isEqual:]
+ -[NTPBCKDate mergeFrom:]
+ -[NTPBCKDate readFrom:]
+ -[NTPBCKDate setHasTime:]
+ -[NTPBCKDate setTime:]
+ -[NTPBCKDate time]
+ -[NTPBCKDate writeTo:]
+ -[NTPBCKDateStatistics .cxx_destruct]
+ -[NTPBCKDateStatistics copyWithZone:]
+ -[NTPBCKDateStatistics creation]
+ -[NTPBCKDateStatistics description]
+ -[NTPBCKDateStatistics dictionaryRepresentation]
+ -[NTPBCKDateStatistics hasCreation]
+ -[NTPBCKDateStatistics hasModification]
+ -[NTPBCKDateStatistics hash]
+ -[NTPBCKDateStatistics isEqual:]
+ -[NTPBCKDateStatistics mergeFrom:]
+ -[NTPBCKDateStatistics modification]
+ -[NTPBCKDateStatistics readFrom:]
+ -[NTPBCKDateStatistics setCreation:]
+ -[NTPBCKDateStatistics setModification:]
+ -[NTPBCKDateStatistics writeTo:]
+ -[NTPBCKIdentifier .cxx_destruct]
+ -[NTPBCKIdentifier copyWithZone:]
+ -[NTPBCKIdentifier description]
+ -[NTPBCKIdentifier dictionaryRepresentation]
+ -[NTPBCKIdentifier hasName]
+ -[NTPBCKIdentifier hasType]
+ -[NTPBCKIdentifier hash]
+ -[NTPBCKIdentifier isEqual:]
+ -[NTPBCKIdentifier mergeFrom:]
+ -[NTPBCKIdentifier name]
+ -[NTPBCKIdentifier readFrom:]
+ -[NTPBCKIdentifier setHasType:]
+ -[NTPBCKIdentifier setName:]
+ -[NTPBCKIdentifier setType:]
+ -[NTPBCKIdentifier type]
+ -[NTPBCKIdentifier writeTo:]
+ -[NTPBCKLocale .cxx_destruct]
+ -[NTPBCKLocale activeKeyboard]
+ -[NTPBCKLocale addEnabledKeyboards:]
+ -[NTPBCKLocale clearEnabledKeyboards]
+ -[NTPBCKLocale copyWithZone:]
+ -[NTPBCKLocale description]
+ -[NTPBCKLocale dictionaryRepresentation]
+ -[NTPBCKLocale enabledKeyboardsAtIndex:]
+ -[NTPBCKLocale enabledKeyboardsCount]
+ -[NTPBCKLocale enabledKeyboards]
+ -[NTPBCKLocale hasActiveKeyboard]
+ -[NTPBCKLocale hasLanguageCode]
+ -[NTPBCKLocale hasRegionCode]
+ -[NTPBCKLocale hash]
+ -[NTPBCKLocale isEqual:]
+ -[NTPBCKLocale languageCode]
+ -[NTPBCKLocale mergeFrom:]
+ -[NTPBCKLocale readFrom:]
+ -[NTPBCKLocale regionCode]
+ -[NTPBCKLocale setActiveKeyboard:]
+ -[NTPBCKLocale setEnabledKeyboards:]
+ -[NTPBCKLocale setLanguageCode:]
+ -[NTPBCKLocale setRegionCode:]
+ -[NTPBCKLocale writeTo:]
+ -[NTPBCKOperation .cxx_destruct]
+ -[NTPBCKOperation copyWithZone:]
+ -[NTPBCKOperation description]
+ -[NTPBCKOperation dictionaryRepresentation]
+ -[NTPBCKOperation hasLast]
+ -[NTPBCKOperation hasOperationUUID]
+ -[NTPBCKOperation hasSynchronousMode]
+ -[NTPBCKOperation hasType]
+ -[NTPBCKOperation hash]
+ -[NTPBCKOperation isEqual:]
+ -[NTPBCKOperation last]
+ -[NTPBCKOperation mergeFrom:]
+ -[NTPBCKOperation operationUUID]
+ -[NTPBCKOperation readFrom:]
+ -[NTPBCKOperation setHasLast:]
+ -[NTPBCKOperation setHasSynchronousMode:]
+ -[NTPBCKOperation setHasType:]
+ -[NTPBCKOperation setLast:]
+ -[NTPBCKOperation setOperationUUID:]
+ -[NTPBCKOperation setSynchronousMode:]
+ -[NTPBCKOperation setType:]
+ -[NTPBCKOperation synchronousMode]
+ -[NTPBCKOperation type]
+ -[NTPBCKOperation writeTo:]
+ -[NTPBCKQuery .cxx_destruct]
+ -[NTPBCKQuery addFilters:]
+ -[NTPBCKQuery addSorts:]
+ -[NTPBCKQuery addTypes:]
+ -[NTPBCKQuery clearFilters]
+ -[NTPBCKQuery clearSorts]
+ -[NTPBCKQuery clearTypes]
+ -[NTPBCKQuery copyWithZone:]
+ -[NTPBCKQuery description]
+ -[NTPBCKQuery dictionaryRepresentation]
+ -[NTPBCKQuery distinct]
+ -[NTPBCKQuery filtersAtIndex:]
+ -[NTPBCKQuery filtersCount]
+ -[NTPBCKQuery filters]
+ -[NTPBCKQuery hasDistinct]
+ -[NTPBCKQuery hasQueryOperator]
+ -[NTPBCKQuery hash]
+ -[NTPBCKQuery isEqual:]
+ -[NTPBCKQuery mergeFrom:]
+ -[NTPBCKQuery queryOperator]
+ -[NTPBCKQuery readFrom:]
+ -[NTPBCKQuery setDistinct:]
+ -[NTPBCKQuery setFilters:]
+ -[NTPBCKQuery setHasDistinct:]
+ -[NTPBCKQuery setHasQueryOperator:]
+ -[NTPBCKQuery setQueryOperator:]
+ -[NTPBCKQuery setSorts:]
+ -[NTPBCKQuery setTypes:]
+ -[NTPBCKQuery sortsAtIndex:]
+ -[NTPBCKQuery sortsCount]
+ -[NTPBCKQuery sorts]
+ -[NTPBCKQuery typesAtIndex:]
+ -[NTPBCKQuery typesCount]
+ -[NTPBCKQuery types]
+ -[NTPBCKQuery writeTo:]
+ -[NTPBCKQueryFilter .cxx_destruct]
+ -[NTPBCKQueryFilter copyWithZone:]
+ -[NTPBCKQueryFilter description]
+ -[NTPBCKQueryFilter dictionaryRepresentation]
+ -[NTPBCKQueryFilter fieldName]
+ -[NTPBCKQueryFilter fieldValue]
+ -[NTPBCKQueryFilter hasFieldName]
+ -[NTPBCKQueryFilter hasFieldValue]
+ -[NTPBCKQueryFilter hasType]
+ -[NTPBCKQueryFilter hash]
+ -[NTPBCKQueryFilter isEqual:]
+ -[NTPBCKQueryFilter mergeFrom:]
+ -[NTPBCKQueryFilter readFrom:]
+ -[NTPBCKQueryFilter setFieldName:]
+ -[NTPBCKQueryFilter setFieldValue:]
+ -[NTPBCKQueryFilter setHasType:]
+ -[NTPBCKQueryFilter setType:]
+ -[NTPBCKQueryFilter type]
+ -[NTPBCKQueryFilter writeTo:]
+ -[NTPBCKQueryRetrieveRequest .cxx_destruct]
+ -[NTPBCKQueryRetrieveRequest continuationMarker]
+ -[NTPBCKQueryRetrieveRequest copyWithZone:]
+ -[NTPBCKQueryRetrieveRequest description]
+ -[NTPBCKQueryRetrieveRequest dictionaryRepresentation]
+ -[NTPBCKQueryRetrieveRequest hasContinuationMarker]
+ -[NTPBCKQueryRetrieveRequest hasLimit]
+ -[NTPBCKQueryRetrieveRequest hasQuery]
+ -[NTPBCKQueryRetrieveRequest hasRequestedFields]
+ -[NTPBCKQueryRetrieveRequest hasZoneIdentifier]
+ -[NTPBCKQueryRetrieveRequest hash]
+ -[NTPBCKQueryRetrieveRequest isEqual:]
+ -[NTPBCKQueryRetrieveRequest limit]
+ -[NTPBCKQueryRetrieveRequest mergeFrom:]
+ -[NTPBCKQueryRetrieveRequest query]
+ -[NTPBCKQueryRetrieveRequest readFrom:]
+ -[NTPBCKQueryRetrieveRequest requestedFields]
+ -[NTPBCKQueryRetrieveRequest setContinuationMarker:]
+ -[NTPBCKQueryRetrieveRequest setHasLimit:]
+ -[NTPBCKQueryRetrieveRequest setLimit:]
+ -[NTPBCKQueryRetrieveRequest setQuery:]
+ -[NTPBCKQueryRetrieveRequest setRequestedFields:]
+ -[NTPBCKQueryRetrieveRequest setZoneIdentifier:]
+ -[NTPBCKQueryRetrieveRequest writeTo:]
+ -[NTPBCKQueryRetrieveRequest zoneIdentifier]
+ -[NTPBCKQueryRetrieveResponse .cxx_destruct]
+ -[NTPBCKQueryRetrieveResponse addQueryResults:]
+ -[NTPBCKQueryRetrieveResponse clearQueryResults]
+ -[NTPBCKQueryRetrieveResponse continuationMarker]
+ -[NTPBCKQueryRetrieveResponse copyWithZone:]
+ -[NTPBCKQueryRetrieveResponse description]
+ -[NTPBCKQueryRetrieveResponse dictionaryRepresentation]
+ -[NTPBCKQueryRetrieveResponse hasContinuationMarker]
+ -[NTPBCKQueryRetrieveResponse hash]
+ -[NTPBCKQueryRetrieveResponse isEqual:]
+ -[NTPBCKQueryRetrieveResponse mergeFrom:]
+ -[NTPBCKQueryRetrieveResponse queryResultsAtIndex:]
+ -[NTPBCKQueryRetrieveResponse queryResultsCount]
+ -[NTPBCKQueryRetrieveResponse queryResults]
+ -[NTPBCKQueryRetrieveResponse readFrom:]
+ -[NTPBCKQueryRetrieveResponse setContinuationMarker:]
+ -[NTPBCKQueryRetrieveResponse setQueryResults:]
+ -[NTPBCKQueryRetrieveResponse writeTo:]
+ -[NTPBCKQueryRetrieveResponseQueryResult .cxx_destruct]
+ -[NTPBCKQueryRetrieveResponseQueryResult copyWithZone:]
+ -[NTPBCKQueryRetrieveResponseQueryResult description]
+ -[NTPBCKQueryRetrieveResponseQueryResult dictionaryRepresentation]
+ -[NTPBCKQueryRetrieveResponseQueryResult etag]
+ -[NTPBCKQueryRetrieveResponseQueryResult hasEtag]
+ -[NTPBCKQueryRetrieveResponseQueryResult hasIdentifier]
+ -[NTPBCKQueryRetrieveResponseQueryResult hasRecord]
+ -[NTPBCKQueryRetrieveResponseQueryResult hasType]
+ -[NTPBCKQueryRetrieveResponseQueryResult hash]
+ -[NTPBCKQueryRetrieveResponseQueryResult identifier]
+ -[NTPBCKQueryRetrieveResponseQueryResult isEqual:]
+ -[NTPBCKQueryRetrieveResponseQueryResult mergeFrom:]
+ -[NTPBCKQueryRetrieveResponseQueryResult readFrom:]
+ -[NTPBCKQueryRetrieveResponseQueryResult record]
+ -[NTPBCKQueryRetrieveResponseQueryResult setEtag:]
+ -[NTPBCKQueryRetrieveResponseQueryResult setHasType:]
+ -[NTPBCKQueryRetrieveResponseQueryResult setIdentifier:]
+ -[NTPBCKQueryRetrieveResponseQueryResult setRecord:]
+ -[NTPBCKQueryRetrieveResponseQueryResult setType:]
+ -[NTPBCKQueryRetrieveResponseQueryResult type]
+ -[NTPBCKQueryRetrieveResponseQueryResult writeTo:]
+ -[NTPBCKQuerySort .cxx_destruct]
+ -[NTPBCKQuerySort copyWithZone:]
+ -[NTPBCKQuerySort description]
+ -[NTPBCKQuerySort dictionaryRepresentation]
+ -[NTPBCKQuerySort fieldName]
+ -[NTPBCKQuerySort hasFieldName]
+ -[NTPBCKQuerySort hasOrder]
+ -[NTPBCKQuerySort hash]
+ -[NTPBCKQuerySort isEqual:]
+ -[NTPBCKQuerySort mergeFrom:]
+ -[NTPBCKQuerySort order]
+ -[NTPBCKQuerySort readFrom:]
+ -[NTPBCKQuerySort setFieldName:]
+ -[NTPBCKQuerySort setHasOrder:]
+ -[NTPBCKQuerySort setOrder:]
+ -[NTPBCKQuerySort writeTo:]
+ -[NTPBCKRecord .cxx_destruct]
+ -[NTPBCKRecord addFields:]
+ -[NTPBCKRecord clearFields]
+ -[NTPBCKRecord copyWithZone:]
+ -[NTPBCKRecord description]
+ -[NTPBCKRecord dictionaryRepresentation]
+ -[NTPBCKRecord etag]
+ -[NTPBCKRecord fieldsAtIndex:]
+ -[NTPBCKRecord fieldsCount]
+ -[NTPBCKRecord fields]
+ -[NTPBCKRecord hasEtag]
+ -[NTPBCKRecord hasRecordIdentifier]
+ -[NTPBCKRecord hasTimeStatistics]
+ -[NTPBCKRecord hasType]
+ -[NTPBCKRecord hash]
+ -[NTPBCKRecord isEqual:]
+ -[NTPBCKRecord mergeFrom:]
+ -[NTPBCKRecord readFrom:]
+ -[NTPBCKRecord recordIdentifier]
+ -[NTPBCKRecord setEtag:]
+ -[NTPBCKRecord setFields:]
+ -[NTPBCKRecord setRecordIdentifier:]
+ -[NTPBCKRecord setTimeStatistics:]
+ -[NTPBCKRecord setType:]
+ -[NTPBCKRecord timeStatistics]
+ -[NTPBCKRecord type]
+ -[NTPBCKRecord writeTo:]
+ -[NTPBCKRecordField .cxx_destruct]
+ -[NTPBCKRecordField copyWithZone:]
+ -[NTPBCKRecordField description]
+ -[NTPBCKRecordField dictionaryRepresentation]
+ -[NTPBCKRecordField hasIdentifier]
+ -[NTPBCKRecordField hasValue]
+ -[NTPBCKRecordField hash]
+ -[NTPBCKRecordField identifier]
+ -[NTPBCKRecordField isEqual:]
+ -[NTPBCKRecordField mergeFrom:]
+ -[NTPBCKRecordField readFrom:]
+ -[NTPBCKRecordField setIdentifier:]
+ -[NTPBCKRecordField setValue:]
+ -[NTPBCKRecordField value]
+ -[NTPBCKRecordField writeTo:]
+ -[NTPBCKRecordFieldIdentifier .cxx_destruct]
+ -[NTPBCKRecordFieldIdentifier copyWithZone:]
+ -[NTPBCKRecordFieldIdentifier description]
+ -[NTPBCKRecordFieldIdentifier dictionaryRepresentation]
+ -[NTPBCKRecordFieldIdentifier hasName]
+ -[NTPBCKRecordFieldIdentifier hash]
+ -[NTPBCKRecordFieldIdentifier isEqual:]
+ -[NTPBCKRecordFieldIdentifier mergeFrom:]
+ -[NTPBCKRecordFieldIdentifier name]
+ -[NTPBCKRecordFieldIdentifier readFrom:]
+ -[NTPBCKRecordFieldIdentifier setName:]
+ -[NTPBCKRecordFieldIdentifier writeTo:]
+ -[NTPBCKRecordFieldValue .cxx_destruct]
+ -[NTPBCKRecordFieldValue addListValue:]
+ -[NTPBCKRecordFieldValue bytesValue]
+ -[NTPBCKRecordFieldValue clearListValues]
+ -[NTPBCKRecordFieldValue copyWithZone:]
+ -[NTPBCKRecordFieldValue dateValue]
+ -[NTPBCKRecordFieldValue description]
+ -[NTPBCKRecordFieldValue dictionaryRepresentation]
+ -[NTPBCKRecordFieldValue doubleValue]
+ -[NTPBCKRecordFieldValue hasBytesValue]
+ -[NTPBCKRecordFieldValue hasDateValue]
+ -[NTPBCKRecordFieldValue hasDoubleValue]
+ -[NTPBCKRecordFieldValue hasReferenceValue]
+ -[NTPBCKRecordFieldValue hasSignedValue]
+ -[NTPBCKRecordFieldValue hasStringValue]
+ -[NTPBCKRecordFieldValue hasType]
+ -[NTPBCKRecordFieldValue hash]
+ -[NTPBCKRecordFieldValue isEqual:]
+ -[NTPBCKRecordFieldValue listValueAtIndex:]
+ -[NTPBCKRecordFieldValue listValuesCount]
+ -[NTPBCKRecordFieldValue listValues]
+ -[NTPBCKRecordFieldValue mergeFrom:]
+ -[NTPBCKRecordFieldValue readFrom:]
+ -[NTPBCKRecordFieldValue referenceValue]
+ -[NTPBCKRecordFieldValue setBytesValue:]
+ -[NTPBCKRecordFieldValue setDateValue:]
+ -[NTPBCKRecordFieldValue setDoubleValue:]
+ -[NTPBCKRecordFieldValue setHasDoubleValue:]
+ -[NTPBCKRecordFieldValue setHasSignedValue:]
+ -[NTPBCKRecordFieldValue setHasType:]
+ -[NTPBCKRecordFieldValue setListValues:]
+ -[NTPBCKRecordFieldValue setReferenceValue:]
+ -[NTPBCKRecordFieldValue setSignedValue:]
+ -[NTPBCKRecordFieldValue setStringValue:]
+ -[NTPBCKRecordFieldValue setType:]
+ -[NTPBCKRecordFieldValue signedValue]
+ -[NTPBCKRecordFieldValue stringValue]
+ -[NTPBCKRecordFieldValue type]
+ -[NTPBCKRecordFieldValue writeTo:]
+ -[NTPBCKRecordIdentifier .cxx_destruct]
+ -[NTPBCKRecordIdentifier copyWithZone:]
+ -[NTPBCKRecordIdentifier description]
+ -[NTPBCKRecordIdentifier dictionaryRepresentation]
+ -[NTPBCKRecordIdentifier hasValue]
+ -[NTPBCKRecordIdentifier hasZoneIdentifier]
+ -[NTPBCKRecordIdentifier hash]
+ -[NTPBCKRecordIdentifier isEqual:]
+ -[NTPBCKRecordIdentifier mergeFrom:]
+ -[NTPBCKRecordIdentifier readFrom:]
+ -[NTPBCKRecordIdentifier setValue:]
+ -[NTPBCKRecordIdentifier setZoneIdentifier:]
+ -[NTPBCKRecordIdentifier value]
+ -[NTPBCKRecordIdentifier writeTo:]
+ -[NTPBCKRecordIdentifier zoneIdentifier]
+ -[NTPBCKRecordReference .cxx_destruct]
+ -[NTPBCKRecordReference copyWithZone:]
+ -[NTPBCKRecordReference description]
+ -[NTPBCKRecordReference dictionaryRepresentation]
+ -[NTPBCKRecordReference hasRecordIdentifier]
+ -[NTPBCKRecordReference hasType]
+ -[NTPBCKRecordReference hash]
+ -[NTPBCKRecordReference isEqual:]
+ -[NTPBCKRecordReference mergeFrom:]
+ -[NTPBCKRecordReference readFrom:]
+ -[NTPBCKRecordReference recordIdentifier]
+ -[NTPBCKRecordReference setHasType:]
+ -[NTPBCKRecordReference setRecordIdentifier:]
+ -[NTPBCKRecordReference setType:]
+ -[NTPBCKRecordReference type]
+ -[NTPBCKRecordReference writeTo:]
+ -[NTPBCKRecordRetrieveRequest .cxx_destruct]
+ -[NTPBCKRecordRetrieveRequest clientVersionETag]
+ -[NTPBCKRecordRetrieveRequest copyWithZone:]
+ -[NTPBCKRecordRetrieveRequest description]
+ -[NTPBCKRecordRetrieveRequest dictionaryRepresentation]
+ -[NTPBCKRecordRetrieveRequest hasClientVersionETag]
+ -[NTPBCKRecordRetrieveRequest hasRecordIdentifier]
+ -[NTPBCKRecordRetrieveRequest hasRequestedFields]
+ -[NTPBCKRecordRetrieveRequest hasVersionETag]
+ -[NTPBCKRecordRetrieveRequest hash]
+ -[NTPBCKRecordRetrieveRequest isEqual:]
+ -[NTPBCKRecordRetrieveRequest mergeFrom:]
+ -[NTPBCKRecordRetrieveRequest readFrom:]
+ -[NTPBCKRecordRetrieveRequest recordIdentifier]
+ -[NTPBCKRecordRetrieveRequest requestedFields]
+ -[NTPBCKRecordRetrieveRequest setClientVersionETag:]
+ -[NTPBCKRecordRetrieveRequest setRecordIdentifier:]
+ -[NTPBCKRecordRetrieveRequest setRequestedFields:]
+ -[NTPBCKRecordRetrieveRequest setVersionETag:]
+ -[NTPBCKRecordRetrieveRequest versionETag]
+ -[NTPBCKRecordRetrieveRequest writeTo:]
+ -[NTPBCKRecordRetrieveResponse .cxx_destruct]
+ -[NTPBCKRecordRetrieveResponse copyWithZone:]
+ -[NTPBCKRecordRetrieveResponse description]
+ -[NTPBCKRecordRetrieveResponse dictionaryRepresentation]
+ -[NTPBCKRecordRetrieveResponse hasRecord]
+ -[NTPBCKRecordRetrieveResponse hash]
+ -[NTPBCKRecordRetrieveResponse isEqual:]
+ -[NTPBCKRecordRetrieveResponse mergeFrom:]
+ -[NTPBCKRecordRetrieveResponse readFrom:]
+ -[NTPBCKRecordRetrieveResponse record]
+ -[NTPBCKRecordRetrieveResponse setRecord:]
+ -[NTPBCKRecordRetrieveResponse writeTo:]
+ -[NTPBCKRecordType .cxx_destruct]
+ -[NTPBCKRecordType copyWithZone:]
+ -[NTPBCKRecordType description]
+ -[NTPBCKRecordType dictionaryRepresentation]
+ -[NTPBCKRecordType hasName]
+ -[NTPBCKRecordType hash]
+ -[NTPBCKRecordType isEqual:]
+ -[NTPBCKRecordType mergeFrom:]
+ -[NTPBCKRecordType name]
+ -[NTPBCKRecordType readFrom:]
+ -[NTPBCKRecordType setName:]
+ -[NTPBCKRecordType writeTo:]
+ -[NTPBCKRecordZoneIdentifier .cxx_destruct]
+ -[NTPBCKRecordZoneIdentifier copyWithZone:]
+ -[NTPBCKRecordZoneIdentifier description]
+ -[NTPBCKRecordZoneIdentifier dictionaryRepresentation]
+ -[NTPBCKRecordZoneIdentifier hasOwnerIdentifier]
+ -[NTPBCKRecordZoneIdentifier hasValue]
+ -[NTPBCKRecordZoneIdentifier hash]
+ -[NTPBCKRecordZoneIdentifier isEqual:]
+ -[NTPBCKRecordZoneIdentifier mergeFrom:]
+ -[NTPBCKRecordZoneIdentifier ownerIdentifier]
+ -[NTPBCKRecordZoneIdentifier readFrom:]
+ -[NTPBCKRecordZoneIdentifier setOwnerIdentifier:]
+ -[NTPBCKRecordZoneIdentifier setValue:]
+ -[NTPBCKRecordZoneIdentifier value]
+ -[NTPBCKRecordZoneIdentifier writeTo:]
+ -[NTPBCKRequestOperation .cxx_destruct]
+ -[NTPBCKRequestOperation copyWithZone:]
+ -[NTPBCKRequestOperation description]
+ -[NTPBCKRequestOperation dictionaryRepresentation]
+ -[NTPBCKRequestOperation hasHeader]
+ -[NTPBCKRequestOperation hasQueryRetrieveRequest]
+ -[NTPBCKRequestOperation hasRecordRetrieveRequest]
+ -[NTPBCKRequestOperation hasRequest]
+ -[NTPBCKRequestOperation hash]
+ -[NTPBCKRequestOperation header]
+ -[NTPBCKRequestOperation isEqual:]
+ -[NTPBCKRequestOperation mergeFrom:]
+ -[NTPBCKRequestOperation queryRetrieveRequest]
+ -[NTPBCKRequestOperation readFrom:]
+ -[NTPBCKRequestOperation recordRetrieveRequest]
+ -[NTPBCKRequestOperation request]
+ -[NTPBCKRequestOperation setHeader:]
+ -[NTPBCKRequestOperation setQueryRetrieveRequest:]
+ -[NTPBCKRequestOperation setRecordRetrieveRequest:]
+ -[NTPBCKRequestOperation setRequest:]
+ -[NTPBCKRequestOperation writeTo:]
+ -[NTPBCKRequestOperationHeader .cxx_destruct]
+ -[NTPBCKRequestOperationHeader applicationBundle]
+ -[NTPBCKRequestOperationHeader applicationConfigVersion]
+ -[NTPBCKRequestOperationHeader applicationContainerEnvironment]
+ -[NTPBCKRequestOperationHeader applicationContainer]
+ -[NTPBCKRequestOperationHeader applicationVersion]
+ -[NTPBCKRequestOperationHeader clientChangeToken]
+ -[NTPBCKRequestOperationHeader copyWithZone:]
+ -[NTPBCKRequestOperationHeader description]
+ -[NTPBCKRequestOperationHeader deviceAssignedName]
+ -[NTPBCKRequestOperationHeader deviceFlowControlBudgetCap]
+ -[NTPBCKRequestOperationHeader deviceFlowControlBudget]
+ -[NTPBCKRequestOperationHeader deviceFlowControlKey]
+ -[NTPBCKRequestOperationHeader deviceFlowControlRegeneration]
+ -[NTPBCKRequestOperationHeader deviceHardwareID]
+ -[NTPBCKRequestOperationHeader deviceHardwareVersion]
+ -[NTPBCKRequestOperationHeader deviceIdentifier]
+ -[NTPBCKRequestOperationHeader deviceLibraryName]
+ -[NTPBCKRequestOperationHeader deviceLibraryVersion]
+ -[NTPBCKRequestOperationHeader deviceProtocolVersion]
+ -[NTPBCKRequestOperationHeader deviceSoftwareIsAppleInternal]
+ -[NTPBCKRequestOperationHeader deviceSoftwareVersion]
+ -[NTPBCKRequestOperationHeader dictionaryRepresentation]
+ -[NTPBCKRequestOperationHeader globalConfigVersion]
+ -[NTPBCKRequestOperationHeader hasApplicationBundle]
+ -[NTPBCKRequestOperationHeader hasApplicationConfigVersion]
+ -[NTPBCKRequestOperationHeader hasApplicationContainerEnvironment]
+ -[NTPBCKRequestOperationHeader hasApplicationContainer]
+ -[NTPBCKRequestOperationHeader hasApplicationVersion]
+ -[NTPBCKRequestOperationHeader hasClientChangeToken]
+ -[NTPBCKRequestOperationHeader hasDeviceAssignedName]
+ -[NTPBCKRequestOperationHeader hasDeviceFlowControlBudgetCap]
+ -[NTPBCKRequestOperationHeader hasDeviceFlowControlBudget]
+ -[NTPBCKRequestOperationHeader hasDeviceFlowControlKey]
+ -[NTPBCKRequestOperationHeader hasDeviceFlowControlRegeneration]
+ -[NTPBCKRequestOperationHeader hasDeviceHardwareID]
+ -[NTPBCKRequestOperationHeader hasDeviceHardwareVersion]
+ -[NTPBCKRequestOperationHeader hasDeviceIdentifier]
+ -[NTPBCKRequestOperationHeader hasDeviceLibraryName]
+ -[NTPBCKRequestOperationHeader hasDeviceLibraryVersion]
+ -[NTPBCKRequestOperationHeader hasDeviceProtocolVersion]
+ -[NTPBCKRequestOperationHeader hasDeviceSoftwareIsAppleInternal]
+ -[NTPBCKRequestOperationHeader hasDeviceSoftwareVersion]
+ -[NTPBCKRequestOperationHeader hasGlobalConfigVersion]
+ -[NTPBCKRequestOperationHeader hasIsolationLevel]
+ -[NTPBCKRequestOperationHeader hasLocale]
+ -[NTPBCKRequestOperationHeader hasMmcsProtocolVersion]
+ -[NTPBCKRequestOperationHeader hasOperationGroupName]
+ -[NTPBCKRequestOperationHeader hasOperationGroupQuantity]
+ -[NTPBCKRequestOperationHeader hasTargetDatabase]
+ -[NTPBCKRequestOperationHeader hasUserIDContainerID]
+ -[NTPBCKRequestOperationHeader hash]
+ -[NTPBCKRequestOperationHeader isEqual:]
+ -[NTPBCKRequestOperationHeader isolationLevel]
+ -[NTPBCKRequestOperationHeader locale]
+ -[NTPBCKRequestOperationHeader mergeFrom:]
+ -[NTPBCKRequestOperationHeader mmcsProtocolVersion]
+ -[NTPBCKRequestOperationHeader operationGroupName]
+ -[NTPBCKRequestOperationHeader operationGroupQuantity]
+ -[NTPBCKRequestOperationHeader readFrom:]
+ -[NTPBCKRequestOperationHeader setApplicationBundle:]
+ -[NTPBCKRequestOperationHeader setApplicationConfigVersion:]
+ -[NTPBCKRequestOperationHeader setApplicationContainer:]
+ -[NTPBCKRequestOperationHeader setApplicationContainerEnvironment:]
+ -[NTPBCKRequestOperationHeader setApplicationVersion:]
+ -[NTPBCKRequestOperationHeader setClientChangeToken:]
+ -[NTPBCKRequestOperationHeader setDeviceAssignedName:]
+ -[NTPBCKRequestOperationHeader setDeviceFlowControlBudget:]
+ -[NTPBCKRequestOperationHeader setDeviceFlowControlBudgetCap:]
+ -[NTPBCKRequestOperationHeader setDeviceFlowControlKey:]
+ -[NTPBCKRequestOperationHeader setDeviceFlowControlRegeneration:]
+ -[NTPBCKRequestOperationHeader setDeviceHardwareID:]
+ -[NTPBCKRequestOperationHeader setDeviceHardwareVersion:]
+ -[NTPBCKRequestOperationHeader setDeviceIdentifier:]
+ -[NTPBCKRequestOperationHeader setDeviceLibraryName:]
+ -[NTPBCKRequestOperationHeader setDeviceLibraryVersion:]
+ -[NTPBCKRequestOperationHeader setDeviceProtocolVersion:]
+ -[NTPBCKRequestOperationHeader setDeviceSoftwareIsAppleInternal:]
+ -[NTPBCKRequestOperationHeader setDeviceSoftwareVersion:]
+ -[NTPBCKRequestOperationHeader setGlobalConfigVersion:]
+ -[NTPBCKRequestOperationHeader setHasApplicationConfigVersion:]
+ -[NTPBCKRequestOperationHeader setHasApplicationContainerEnvironment:]
+ -[NTPBCKRequestOperationHeader setHasDeviceFlowControlBudget:]
+ -[NTPBCKRequestOperationHeader setHasDeviceFlowControlBudgetCap:]
+ -[NTPBCKRequestOperationHeader setHasDeviceFlowControlRegeneration:]
+ -[NTPBCKRequestOperationHeader setHasDeviceProtocolVersion:]
+ -[NTPBCKRequestOperationHeader setHasDeviceSoftwareIsAppleInternal:]
+ -[NTPBCKRequestOperationHeader setHasGlobalConfigVersion:]
+ -[NTPBCKRequestOperationHeader setHasIsolationLevel:]
+ -[NTPBCKRequestOperationHeader setHasOperationGroupQuantity:]
+ -[NTPBCKRequestOperationHeader setHasTargetDatabase:]
+ -[NTPBCKRequestOperationHeader setIsolationLevel:]
+ -[NTPBCKRequestOperationHeader setLocale:]
+ -[NTPBCKRequestOperationHeader setMmcsProtocolVersion:]
+ -[NTPBCKRequestOperationHeader setOperationGroupName:]
+ -[NTPBCKRequestOperationHeader setOperationGroupQuantity:]
+ -[NTPBCKRequestOperationHeader setTargetDatabase:]
+ -[NTPBCKRequestOperationHeader setUserIDContainerID:]
+ -[NTPBCKRequestOperationHeader targetDatabase]
+ -[NTPBCKRequestOperationHeader userIDContainerID]
+ -[NTPBCKRequestOperationHeader writeTo:]
+ -[NTPBCKRequestedFields .cxx_destruct]
+ -[NTPBCKRequestedFields addFields:]
+ -[NTPBCKRequestedFields clearFields]
+ -[NTPBCKRequestedFields copyWithZone:]
+ -[NTPBCKRequestedFields description]
+ -[NTPBCKRequestedFields dictionaryRepresentation]
+ -[NTPBCKRequestedFields fieldsAtIndex:]
+ -[NTPBCKRequestedFields fieldsCount]
+ -[NTPBCKRequestedFields fields]
+ -[NTPBCKRequestedFields hash]
+ -[NTPBCKRequestedFields isEqual:]
+ -[NTPBCKRequestedFields mergeFrom:]
+ -[NTPBCKRequestedFields readFrom:]
+ -[NTPBCKRequestedFields setFields:]
+ -[NTPBCKRequestedFields writeTo:]
+ -[NTPBCKResponseOperation .cxx_destruct]
+ -[NTPBCKResponseOperation copyWithZone:]
+ -[NTPBCKResponseOperation description]
+ -[NTPBCKResponseOperation dictionaryRepresentation]
+ -[NTPBCKResponseOperation hasQueryRetrieveResponse]
+ -[NTPBCKResponseOperation hasRecordRetrieveResponse]
+ -[NTPBCKResponseOperation hasResponse]
+ -[NTPBCKResponseOperation hasResult]
+ -[NTPBCKResponseOperation hash]
+ -[NTPBCKResponseOperation isEqual:]
+ -[NTPBCKResponseOperation mergeFrom:]
+ -[NTPBCKResponseOperation queryRetrieveResponse]
+ -[NTPBCKResponseOperation readFrom:]
+ -[NTPBCKResponseOperation recordRetrieveResponse]
+ -[NTPBCKResponseOperation response]
+ -[NTPBCKResponseOperation result]
+ -[NTPBCKResponseOperation setQueryRetrieveResponse:]
+ -[NTPBCKResponseOperation setRecordRetrieveResponse:]
+ -[NTPBCKResponseOperation setResponse:]
+ -[NTPBCKResponseOperation setResult:]
+ -[NTPBCKResponseOperation writeTo:]
+ -[NTPBCKResponseOperationResult .cxx_destruct]
+ -[NTPBCKResponseOperationResult code]
+ -[NTPBCKResponseOperationResult copyWithZone:]
+ -[NTPBCKResponseOperationResult description]
+ -[NTPBCKResponseOperationResult dictionaryRepresentation]
+ -[NTPBCKResponseOperationResult error]
+ -[NTPBCKResponseOperationResult hasCode]
+ -[NTPBCKResponseOperationResult hasError]
+ -[NTPBCKResponseOperationResult hash]
+ -[NTPBCKResponseOperationResult isEqual:]
+ -[NTPBCKResponseOperationResult mergeFrom:]
+ -[NTPBCKResponseOperationResult readFrom:]
+ -[NTPBCKResponseOperationResult setCode:]
+ -[NTPBCKResponseOperationResult setError:]
+ -[NTPBCKResponseOperationResult setHasCode:]
+ -[NTPBCKResponseOperationResult writeTo:]
+ -[NTPBCKResponseOperationResultError .cxx_destruct]
+ -[NTPBCKResponseOperationResultError clientError]
+ -[NTPBCKResponseOperationResultError copyWithZone:]
+ -[NTPBCKResponseOperationResultError description]
+ -[NTPBCKResponseOperationResultError dictionaryRepresentation]
+ -[NTPBCKResponseOperationResultError errorDescription]
+ -[NTPBCKResponseOperationResultError errorKey]
+ -[NTPBCKResponseOperationResultError extensionError]
+ -[NTPBCKResponseOperationResultError hasClientError]
+ -[NTPBCKResponseOperationResultError hasErrorDescription]
+ -[NTPBCKResponseOperationResultError hasErrorKey]
+ -[NTPBCKResponseOperationResultError hasExtensionError]
+ -[NTPBCKResponseOperationResultError hasRetryAfterSeconds]
+ -[NTPBCKResponseOperationResultError hasServerError]
+ -[NTPBCKResponseOperationResultError hash]
+ -[NTPBCKResponseOperationResultError isEqual:]
+ -[NTPBCKResponseOperationResultError mergeFrom:]
+ -[NTPBCKResponseOperationResultError readFrom:]
+ -[NTPBCKResponseOperationResultError retryAfterSeconds]
+ -[NTPBCKResponseOperationResultError serverError]
+ -[NTPBCKResponseOperationResultError setClientError:]
+ -[NTPBCKResponseOperationResultError setErrorDescription:]
+ -[NTPBCKResponseOperationResultError setErrorKey:]
+ -[NTPBCKResponseOperationResultError setExtensionError:]
+ -[NTPBCKResponseOperationResultError setHasRetryAfterSeconds:]
+ -[NTPBCKResponseOperationResultError setRetryAfterSeconds:]
+ -[NTPBCKResponseOperationResultError setServerError:]
+ -[NTPBCKResponseOperationResultError writeTo:]
+ -[NTPBCKResponseOperationResultErrorClient copyWithZone:]
+ -[NTPBCKResponseOperationResultErrorClient description]
+ -[NTPBCKResponseOperationResultErrorClient dictionaryRepresentation]
+ -[NTPBCKResponseOperationResultErrorClient hasType]
+ -[NTPBCKResponseOperationResultErrorClient hash]
+ -[NTPBCKResponseOperationResultErrorClient isEqual:]
+ -[NTPBCKResponseOperationResultErrorClient mergeFrom:]
+ -[NTPBCKResponseOperationResultErrorClient readFrom:]
+ -[NTPBCKResponseOperationResultErrorClient setHasType:]
+ -[NTPBCKResponseOperationResultErrorClient setType:]
+ -[NTPBCKResponseOperationResultErrorClient type]
+ -[NTPBCKResponseOperationResultErrorClient writeTo:]
+ -[NTPBCKResponseOperationResultErrorExtension .cxx_destruct]
+ -[NTPBCKResponseOperationResultErrorExtension copyWithZone:]
+ -[NTPBCKResponseOperationResultErrorExtension description]
+ -[NTPBCKResponseOperationResultErrorExtension dictionaryRepresentation]
+ -[NTPBCKResponseOperationResultErrorExtension extensionName]
+ -[NTPBCKResponseOperationResultErrorExtension extensionPayload]
+ -[NTPBCKResponseOperationResultErrorExtension hasExtensionName]
+ -[NTPBCKResponseOperationResultErrorExtension hasExtensionPayload]
+ -[NTPBCKResponseOperationResultErrorExtension hasTypeCode]
+ -[NTPBCKResponseOperationResultErrorExtension hash]
+ -[NTPBCKResponseOperationResultErrorExtension isEqual:]
+ -[NTPBCKResponseOperationResultErrorExtension mergeFrom:]
+ -[NTPBCKResponseOperationResultErrorExtension readFrom:]
+ -[NTPBCKResponseOperationResultErrorExtension setExtensionName:]
+ -[NTPBCKResponseOperationResultErrorExtension setExtensionPayload:]
+ -[NTPBCKResponseOperationResultErrorExtension setHasTypeCode:]
+ -[NTPBCKResponseOperationResultErrorExtension setTypeCode:]
+ -[NTPBCKResponseOperationResultErrorExtension typeCode]
+ -[NTPBCKResponseOperationResultErrorExtension writeTo:]
+ -[NTPBCKResponseOperationResultErrorServer copyWithZone:]
+ -[NTPBCKResponseOperationResultErrorServer description]
+ -[NTPBCKResponseOperationResultErrorServer dictionaryRepresentation]
+ -[NTPBCKResponseOperationResultErrorServer hasType]
+ -[NTPBCKResponseOperationResultErrorServer hash]
+ -[NTPBCKResponseOperationResultErrorServer isEqual:]
+ -[NTPBCKResponseOperationResultErrorServer mergeFrom:]
+ -[NTPBCKResponseOperationResultErrorServer readFrom:]
+ -[NTPBCKResponseOperationResultErrorServer setHasType:]
+ -[NTPBCKResponseOperationResultErrorServer setType:]
+ -[NTPBCKResponseOperationResultErrorServer type]
+ -[NTPBCKResponseOperationResultErrorServer writeTo:]
+ -[NTPBFeedItem hasStoryType]
+ -[NTPBFeedItem hasSurfacedByChannelID]
+ -[NTPBFeedItem hasSurfacedByFlags]
+ -[NTPBFeedItem hasSurfacedBySectionID]
+ -[NTPBFeedItem hasSurfacedByTopicID]
+ -[NTPBFeedItem setHasStoryType:]
+ -[NTPBFeedItem setHasSurfacedByFlags:]
+ -[NTPBFeedItem setStoryType:]
+ -[NTPBFeedItem setSurfacedByChannelID:]
+ -[NTPBFeedItem setSurfacedByFlags:]
+ -[NTPBFeedItem setSurfacedBySectionID:]
+ -[NTPBFeedItem setSurfacedByTopicID:]
+ -[NTPBFeedItem storyType]
+ -[NTPBFeedItem surfacedByChannelID]
+ -[NTPBFeedItem surfacedByFlags]
+ -[NTPBFeedItem surfacedBySectionID]
+ -[NTPBFeedItem surfacedByTopicID]
+ -[NTPBFetchRecordSpec .cxx_destruct]
+ -[NTPBFetchRecordSpec addDesiredFields:]
+ -[NTPBFetchRecordSpec addLinkedFields:]
+ -[NTPBFetchRecordSpec clearDesiredFields]
+ -[NTPBFetchRecordSpec clearLinkedFields]
+ -[NTPBFetchRecordSpec copyWithZone:]
+ -[NTPBFetchRecordSpec description]
+ -[NTPBFetchRecordSpec desiredFieldsAtIndex:]
+ -[NTPBFetchRecordSpec desiredFieldsCount]
+ -[NTPBFetchRecordSpec desiredFields]
+ -[NTPBFetchRecordSpec dictionaryRepresentation]
+ -[NTPBFetchRecordSpec hasRecordType]
+ -[NTPBFetchRecordSpec hash]
+ -[NTPBFetchRecordSpec isEqual:]
+ -[NTPBFetchRecordSpec linkedFieldsAtIndex:]
+ -[NTPBFetchRecordSpec linkedFieldsCount]
+ -[NTPBFetchRecordSpec linkedFields]
+ -[NTPBFetchRecordSpec mergeFrom:]
+ -[NTPBFetchRecordSpec readFrom:]
+ -[NTPBFetchRecordSpec recordType]
+ -[NTPBFetchRecordSpec setDesiredFields:]
+ -[NTPBFetchRecordSpec setLinkedFields:]
+ -[NTPBFetchRecordSpec setRecordType:]
+ -[NTPBFetchRecordSpec writeTo:]
+ -[NTPBForYouTodaySectionSpecificConfig feedItemMaxCount]
+ -[NTPBForYouTodaySectionSpecificConfig hasFeedItemMaxCount]
+ -[NTPBForYouTodaySectionSpecificConfig setFeedItemMaxCount:]
+ -[NTPBForYouTodaySectionSpecificConfig setHasFeedItemMaxCount:]
+ -[NTPBNetworkEvent addSmarterFetchSources:]
+ -[NTPBNetworkEvent clearSmarterFetchSources]
+ -[NTPBNetworkEvent hasSmarterFetchStrategy]
+ -[NTPBNetworkEvent setSmarterFetchSources:]
+ -[NTPBNetworkEvent setSmarterFetchStrategy:]
+ -[NTPBNetworkEvent smarterFetchSourcesAtIndex:]
+ -[NTPBNetworkEvent smarterFetchSourcesCount]
+ -[NTPBNetworkEvent smarterFetchSources]
+ -[NTPBNetworkEvent smarterFetchStrategy]
+ -[NTPBPersonalizationParams .cxx_destruct]
+ -[NTPBPersonalizationParams copyWithZone:]
+ -[NTPBPersonalizationParams description]
+ -[NTPBPersonalizationParams dictionaryRepresentation]
+ -[NTPBPersonalizationParams hasUivModelId]
+ -[NTPBPersonalizationParams hasUserInterestVector]
+ -[NTPBPersonalizationParams hash]
+ -[NTPBPersonalizationParams isEqual:]
+ -[NTPBPersonalizationParams mergeFrom:]
+ -[NTPBPersonalizationParams readFrom:]
+ -[NTPBPersonalizationParams setUivModelId:]
+ -[NTPBPersonalizationParams setUserInterestVector:]
+ -[NTPBPersonalizationParams uivModelId]
+ -[NTPBPersonalizationParams userInterestVector]
+ -[NTPBPersonalizationParams writeTo:]
+ -[NTPBRecipeListRecord addRecipeIDs:]
+ -[NTPBRecipeListRecord base]
+ -[NTPBRecipeListRecord clearRecipeIDs]
+ -[NTPBRecipeListRecord copyWithZone:]
+ -[NTPBRecipeListRecord dealloc]
+ -[NTPBRecipeListRecord description]
+ -[NTPBRecipeListRecord dictionaryRepresentation]
+ -[NTPBRecipeListRecord hasBase]
+ -[NTPBRecipeListRecord hash]
+ -[NTPBRecipeListRecord isEqual:]
+ -[NTPBRecipeListRecord mergeFrom:]
+ -[NTPBRecipeListRecord readFrom:]
+ -[NTPBRecipeListRecord recipeIDsAtIndex:]
+ -[NTPBRecipeListRecord recipeIDsCount]
+ -[NTPBRecipeListRecord recipeIDs]
+ -[NTPBRecipeListRecord setBase:]
+ -[NTPBRecipeListRecord setRecipeIDs:]
+ -[NTPBRecipeListRecord writeTo:]
+ -[NTPBRecipeRecord addAllowedStorefrontIDs:]
+ -[NTPBRecipeRecord addArticleIDs:]
+ -[NTPBRecipeRecord addAuthors:]
+ -[NTPBRecipeRecord addBlockedStorefrontIDs:]
+ -[NTPBRecipeRecord addIAdCategories:]
+ -[NTPBRecipeRecord addIAdKeywords:]
+ -[NTPBRecipeRecord addIAdSectionTagIDs:]
+ -[NTPBRecipeRecord addTopicTagIDs:]
+ -[NTPBRecipeRecord addTopics:]
+ -[NTPBRecipeRecord allowedStorefrontIDsAtIndex:]
+ -[NTPBRecipeRecord allowedStorefrontIDsCount]
+ -[NTPBRecipeRecord allowedStorefrontIDs]
+ -[NTPBRecipeRecord articleIDsAtIndex:]
+ -[NTPBRecipeRecord articleIDsCount]
+ -[NTPBRecipeRecord articleIDs]
+ -[NTPBRecipeRecord authorsAtIndex:]
+ -[NTPBRecipeRecord authorsCount]
+ -[NTPBRecipeRecord authors]
+ -[NTPBRecipeRecord base]
+ -[NTPBRecipeRecord blockedStorefrontIDsAtIndex:]
+ -[NTPBRecipeRecord blockedStorefrontIDsCount]
+ -[NTPBRecipeRecord blockedStorefrontIDs]
+ -[NTPBRecipeRecord clearAllowedStorefrontIDs]
+ -[NTPBRecipeRecord clearArticleIDs]
+ -[NTPBRecipeRecord clearAuthors]
+ -[NTPBRecipeRecord clearBlockedStorefrontIDs]
+ -[NTPBRecipeRecord clearIAdCategories]
+ -[NTPBRecipeRecord clearIAdKeywords]
+ -[NTPBRecipeRecord clearIAdSectionTagIDs]
+ -[NTPBRecipeRecord clearTopicTagIDs]
+ -[NTPBRecipeRecord clearTopics]
+ -[NTPBRecipeRecord contentType]
+ -[NTPBRecipeRecord contentURL]
+ -[NTPBRecipeRecord copyWithZone:]
+ -[NTPBRecipeRecord dealloc]
+ -[NTPBRecipeRecord description]
+ -[NTPBRecipeRecord dictionaryRepresentation]
+ -[NTPBRecipeRecord eventAggregationPersonalizationData]
+ -[NTPBRecipeRecord hasBase]
+ -[NTPBRecipeRecord hasContentType]
+ -[NTPBRecipeRecord hasContentURL]
+ -[NTPBRecipeRecord hasEventAggregationPersonalizationData]
+ -[NTPBRecipeRecord hasIsDraft]
+ -[NTPBRecipeRecord hasIsPaid]
+ -[NTPBRecipeRecord hasLanguage]
+ -[NTPBRecipeRecord hasLastReferenceDate]
+ -[NTPBRecipeRecord hasMinimumNewsVersion]
+ -[NTPBRecipeRecord hasPersonalizationData]
+ -[NTPBRecipeRecord hasPublishDate]
+ -[NTPBRecipeRecord hasRapidUpdatePersonalizationData]
+ -[NTPBRecipeRecord hasRecipesRecirculationDataURL]
+ -[NTPBRecipeRecord hasShortExcerpt]
+ -[NTPBRecipeRecord hasSourceChannelTagID]
+ -[NTPBRecipeRecord hasThumbnailAccentColor]
+ -[NTPBRecipeRecord hasThumbnailBackgroundColor]
+ -[NTPBRecipeRecord hasThumbnailExtraLargeMetadata]
+ -[NTPBRecipeRecord hasThumbnailExtraLargeURL]
+ -[NTPBRecipeRecord hasThumbnailFocalFrame]
+ -[NTPBRecipeRecord hasThumbnailLargeMetadata]
+ -[NTPBRecipeRecord hasThumbnailLargeURL]
+ -[NTPBRecipeRecord hasThumbnailMediumMetadata]
+ -[NTPBRecipeRecord hasThumbnailMediumURL]
+ -[NTPBRecipeRecord hasThumbnailPerceptualHash]
+ -[NTPBRecipeRecord hasThumbnailPrimaryColor]
+ -[NTPBRecipeRecord hasThumbnailSmallMetadata]
+ -[NTPBRecipeRecord hasThumbnailSmallURL]
+ -[NTPBRecipeRecord hasThumbnailTextColor]
+ -[NTPBRecipeRecord hasTitle]
+ -[NTPBRecipeRecord hasTotalTime]
+ -[NTPBRecipeRecord hash]
+ -[NTPBRecipeRecord iAdCategoriesAtIndex:]
+ -[NTPBRecipeRecord iAdCategoriesCount]
+ -[NTPBRecipeRecord iAdCategories]
+ -[NTPBRecipeRecord iAdKeywordsAtIndex:]
+ -[NTPBRecipeRecord iAdKeywordsCount]
+ -[NTPBRecipeRecord iAdKeywords]
+ -[NTPBRecipeRecord iAdSectionTagIDsAtIndex:]
+ -[NTPBRecipeRecord iAdSectionTagIDsCount]
+ -[NTPBRecipeRecord iAdSectionTagIDs]
+ -[NTPBRecipeRecord isDraft]
+ -[NTPBRecipeRecord isEqual:]
+ -[NTPBRecipeRecord isPaid]
+ -[NTPBRecipeRecord language]
+ -[NTPBRecipeRecord lastReferenceDate]
+ -[NTPBRecipeRecord mergeFrom:]
+ -[NTPBRecipeRecord minimumNewsVersion]
+ -[NTPBRecipeRecord personalizationData]
+ -[NTPBRecipeRecord publishDate]
+ -[NTPBRecipeRecord rapidUpdatePersonalizationData]
+ -[NTPBRecipeRecord readFrom:]
+ -[NTPBRecipeRecord recipesRecirculationDataURL]
+ -[NTPBRecipeRecord setAllowedStorefrontIDs:]
+ -[NTPBRecipeRecord setArticleIDs:]
+ -[NTPBRecipeRecord setAuthors:]
+ -[NTPBRecipeRecord setBase:]
+ -[NTPBRecipeRecord setBlockedStorefrontIDs:]
+ -[NTPBRecipeRecord setContentType:]
+ -[NTPBRecipeRecord setContentURL:]
+ -[NTPBRecipeRecord setEventAggregationPersonalizationData:]
+ -[NTPBRecipeRecord setHasIsDraft:]
+ -[NTPBRecipeRecord setHasIsPaid:]
+ -[NTPBRecipeRecord setHasMinimumNewsVersion:]
+ -[NTPBRecipeRecord setHasThumbnailExtraLargeMetadata:]
+ -[NTPBRecipeRecord setHasThumbnailFocalFrame:]
+ -[NTPBRecipeRecord setHasThumbnailLargeMetadata:]
+ -[NTPBRecipeRecord setHasThumbnailMediumMetadata:]
+ -[NTPBRecipeRecord setHasThumbnailSmallMetadata:]
+ -[NTPBRecipeRecord setIAdCategories:]
+ -[NTPBRecipeRecord setIAdKeywords:]
+ -[NTPBRecipeRecord setIAdSectionTagIDs:]
+ -[NTPBRecipeRecord setIsDraft:]
+ -[NTPBRecipeRecord setIsPaid:]
+ -[NTPBRecipeRecord setLanguage:]
+ -[NTPBRecipeRecord setLastReferenceDate:]
+ -[NTPBRecipeRecord setMinimumNewsVersion:]
+ -[NTPBRecipeRecord setPersonalizationData:]
+ -[NTPBRecipeRecord setPublishDate:]
+ -[NTPBRecipeRecord setRapidUpdatePersonalizationData:]
+ -[NTPBRecipeRecord setRecipesRecirculationDataURL:]
+ -[NTPBRecipeRecord setShortExcerpt:]
+ -[NTPBRecipeRecord setSourceChannelTagID:]
+ -[NTPBRecipeRecord setThumbnailAccentColor:]
+ -[NTPBRecipeRecord setThumbnailBackgroundColor:]
+ -[NTPBRecipeRecord setThumbnailExtraLargeMetadata:]
+ -[NTPBRecipeRecord setThumbnailExtraLargeURL:]
+ -[NTPBRecipeRecord setThumbnailFocalFrame:]
+ -[NTPBRecipeRecord setThumbnailLargeMetadata:]
+ -[NTPBRecipeRecord setThumbnailLargeURL:]
+ -[NTPBRecipeRecord setThumbnailMediumMetadata:]
+ -[NTPBRecipeRecord setThumbnailMediumURL:]
+ -[NTPBRecipeRecord setThumbnailPerceptualHash:]
+ -[NTPBRecipeRecord setThumbnailPrimaryColor:]
+ -[NTPBRecipeRecord setThumbnailSmallMetadata:]
+ -[NTPBRecipeRecord setThumbnailSmallURL:]
+ -[NTPBRecipeRecord setThumbnailTextColor:]
+ -[NTPBRecipeRecord setTitle:]
+ -[NTPBRecipeRecord setTopicTagIDs:]
+ -[NTPBRecipeRecord setTopics:]
+ -[NTPBRecipeRecord setTotalTime:]
+ -[NTPBRecipeRecord shortExcerpt]
+ -[NTPBRecipeRecord sourceChannelTagID]
+ -[NTPBRecipeRecord thumbnailAccentColor]
+ -[NTPBRecipeRecord thumbnailBackgroundColor]
+ -[NTPBRecipeRecord thumbnailExtraLargeMetadata]
+ -[NTPBRecipeRecord thumbnailExtraLargeURL]
+ -[NTPBRecipeRecord thumbnailFocalFrame]
+ -[NTPBRecipeRecord thumbnailLargeMetadata]
+ -[NTPBRecipeRecord thumbnailLargeURL]
+ -[NTPBRecipeRecord thumbnailMediumMetadata]
+ -[NTPBRecipeRecord thumbnailMediumURL]
+ -[NTPBRecipeRecord thumbnailPerceptualHash]
+ -[NTPBRecipeRecord thumbnailPrimaryColor]
+ -[NTPBRecipeRecord thumbnailSmallMetadata]
+ -[NTPBRecipeRecord thumbnailSmallURL]
+ -[NTPBRecipeRecord thumbnailTextColor]
+ -[NTPBRecipeRecord title]
+ -[NTPBRecipeRecord topicTagIDsAtIndex:]
+ -[NTPBRecipeRecord topicTagIDsCount]
+ -[NTPBRecipeRecord topicTagIDs]
+ -[NTPBRecipeRecord topicsAtIndex:]
+ -[NTPBRecipeRecord topicsCount]
+ -[NTPBRecipeRecord topics]
+ -[NTPBRecipeRecord totalTime]
+ -[NTPBRecipeRecord writeTo:]
+ -[NTPBSmarterFetchRequest .cxx_destruct]
+ -[NTPBSmarterFetchRequest addTagsFollowed:]
+ -[NTPBSmarterFetchRequest addTodayFeedPoolRequests:]
+ -[NTPBSmarterFetchRequest clearTagsFolloweds]
+ -[NTPBSmarterFetchRequest clearTodayFeedPoolRequests]
+ -[NTPBSmarterFetchRequest copyWithZone:]
+ -[NTPBSmarterFetchRequest description]
+ -[NTPBSmarterFetchRequest dictionaryRepresentation]
+ -[NTPBSmarterFetchRequest hasPersonalizationParams]
+ -[NTPBSmarterFetchRequest hasUserInfo]
+ -[NTPBSmarterFetchRequest hash]
+ -[NTPBSmarterFetchRequest isEqual:]
+ -[NTPBSmarterFetchRequest mergeFrom:]
+ -[NTPBSmarterFetchRequest personalizationParams]
+ -[NTPBSmarterFetchRequest readFrom:]
+ -[NTPBSmarterFetchRequest setPersonalizationParams:]
+ -[NTPBSmarterFetchRequest setTagsFolloweds:]
+ -[NTPBSmarterFetchRequest setTodayFeedPoolRequests:]
+ -[NTPBSmarterFetchRequest setUserInfo:]
+ -[NTPBSmarterFetchRequest tagsFollowedAtIndex:]
+ -[NTPBSmarterFetchRequest tagsFollowedsCount]
+ -[NTPBSmarterFetchRequest tagsFolloweds]
+ -[NTPBSmarterFetchRequest todayFeedPoolRequestsAtIndex:]
+ -[NTPBSmarterFetchRequest todayFeedPoolRequestsCount]
+ -[NTPBSmarterFetchRequest todayFeedPoolRequests]
+ -[NTPBSmarterFetchRequest userInfo]
+ -[NTPBSmarterFetchRequest writeTo:]
+ -[NTPBSmarterFetchResponse .cxx_destruct]
+ -[NTPBSmarterFetchResponse addTodayFeedPoolResponse:]
+ -[NTPBSmarterFetchResponse clearTodayFeedPoolResponses]
+ -[NTPBSmarterFetchResponse copyWithZone:]
+ -[NTPBSmarterFetchResponse description]
+ -[NTPBSmarterFetchResponse dictionaryRepresentation]
+ -[NTPBSmarterFetchResponse hash]
+ -[NTPBSmarterFetchResponse isEqual:]
+ -[NTPBSmarterFetchResponse mergeFrom:]
+ -[NTPBSmarterFetchResponse readFrom:]
+ -[NTPBSmarterFetchResponse setTodayFeedPoolResponses:]
+ -[NTPBSmarterFetchResponse todayFeedPoolResponseAtIndex:]
+ -[NTPBSmarterFetchResponse todayFeedPoolResponsesCount]
+ -[NTPBSmarterFetchResponse todayFeedPoolResponses]
+ -[NTPBSmarterFetchResponse writeTo:]
+ -[NTPBTagFollowed .cxx_destruct]
+ -[NTPBTagFollowed aLaCarteSubscribed]
+ -[NTPBTagFollowed copyWithZone:]
+ -[NTPBTagFollowed description]
+ -[NTPBTagFollowed dictionaryRepresentation]
+ -[NTPBTagFollowed hasALaCarteSubscribed]
+ -[NTPBTagFollowed hasTagFollowMode]
+ -[NTPBTagFollowed hasTagId]
+ -[NTPBTagFollowed hash]
+ -[NTPBTagFollowed isEqual:]
+ -[NTPBTagFollowed mergeFrom:]
+ -[NTPBTagFollowed readFrom:]
+ -[NTPBTagFollowed setALaCarteSubscribed:]
+ -[NTPBTagFollowed setHasALaCarteSubscribed:]
+ -[NTPBTagFollowed setHasTagFollowMode:]
+ -[NTPBTagFollowed setTagFollowMode:]
+ -[NTPBTagFollowed setTagId:]
+ -[NTPBTagFollowed tagFollowMode]
+ -[NTPBTagFollowed tagId]
+ -[NTPBTagFollowed writeTo:]
+ -[NTPBTagRecord foodGroupingAvailability]
+ -[NTPBTagRecord hasFoodGroupingAvailability]
+ -[NTPBTagRecord setFoodGroupingAvailability:]
+ -[NTPBTagRecord setHasFoodGroupingAvailability:]
+ -[NTPBTodayFeedPoolRequest .cxx_destruct]
+ -[NTPBTodayFeedPoolRequest addFetchRecordSpecs:]
+ -[NTPBTodayFeedPoolRequest clearFetchRecordSpecs]
+ -[NTPBTodayFeedPoolRequest copyWithZone:]
+ -[NTPBTodayFeedPoolRequest description]
+ -[NTPBTodayFeedPoolRequest dictionaryRepresentation]
+ -[NTPBTodayFeedPoolRequest fetchRecordSpecsAtIndex:]
+ -[NTPBTodayFeedPoolRequest fetchRecordSpecsCount]
+ -[NTPBTodayFeedPoolRequest fetchRecordSpecs]
+ -[NTPBTodayFeedPoolRequest fetchSource]
+ -[NTPBTodayFeedPoolRequest fetchStrategy]
+ -[NTPBTodayFeedPoolRequest fromTimestamp]
+ -[NTPBTodayFeedPoolRequest hasFetchSource]
+ -[NTPBTodayFeedPoolRequest hasFetchStrategy]
+ -[NTPBTodayFeedPoolRequest hasFromTimestamp]
+ -[NTPBTodayFeedPoolRequest hasPreviousFromTimestamp]
+ -[NTPBTodayFeedPoolRequest hasRequestId]
+ -[NTPBTodayFeedPoolRequest hash]
+ -[NTPBTodayFeedPoolRequest isEqual:]
+ -[NTPBTodayFeedPoolRequest mergeFrom:]
+ -[NTPBTodayFeedPoolRequest previousFromTimestamp]
+ -[NTPBTodayFeedPoolRequest readFrom:]
+ -[NTPBTodayFeedPoolRequest requestId]
+ -[NTPBTodayFeedPoolRequest setFetchRecordSpecs:]
+ -[NTPBTodayFeedPoolRequest setFetchSource:]
+ -[NTPBTodayFeedPoolRequest setFetchStrategy:]
+ -[NTPBTodayFeedPoolRequest setFromTimestamp:]
+ -[NTPBTodayFeedPoolRequest setHasFromTimestamp:]
+ -[NTPBTodayFeedPoolRequest setHasPreviousFromTimestamp:]
+ -[NTPBTodayFeedPoolRequest setPreviousFromTimestamp:]
+ -[NTPBTodayFeedPoolRequest setRequestId:]
+ -[NTPBTodayFeedPoolRequest writeTo:]
+ -[NTPBTodayFeedPoolResponse .cxx_destruct]
+ -[NTPBTodayFeedPoolResponse addRecords:]
+ -[NTPBTodayFeedPoolResponse clearRecords]
+ -[NTPBTodayFeedPoolResponse copyWithZone:]
+ -[NTPBTodayFeedPoolResponse description]
+ -[NTPBTodayFeedPoolResponse dictionaryRepresentation]
+ -[NTPBTodayFeedPoolResponse hasNextFromTimestamp]
+ -[NTPBTodayFeedPoolResponse hasRequestId]
+ -[NTPBTodayFeedPoolResponse hasTtlSecs]
+ -[NTPBTodayFeedPoolResponse hash]
+ -[NTPBTodayFeedPoolResponse isEqual:]
+ -[NTPBTodayFeedPoolResponse mergeFrom:]
+ -[NTPBTodayFeedPoolResponse nextFromTimestamp]
+ -[NTPBTodayFeedPoolResponse readFrom:]
+ -[NTPBTodayFeedPoolResponse recordsAtIndex:]
+ -[NTPBTodayFeedPoolResponse recordsCount]
+ -[NTPBTodayFeedPoolResponse records]
+ -[NTPBTodayFeedPoolResponse requestId]
+ -[NTPBTodayFeedPoolResponse setHasNextFromTimestamp:]
+ -[NTPBTodayFeedPoolResponse setHasTtlSecs:]
+ -[NTPBTodayFeedPoolResponse setNextFromTimestamp:]
+ -[NTPBTodayFeedPoolResponse setRecords:]
+ -[NTPBTodayFeedPoolResponse setRequestId:]
+ -[NTPBTodayFeedPoolResponse setTtlSecs:]
+ -[NTPBTodayFeedPoolResponse ttlSecs]
+ -[NTPBTodayFeedPoolResponse writeTo:]
+ -[NTPBUserInfo .cxx_destruct]
+ -[NTPBUserInfo addPreferredLanguages:]
+ -[NTPBUserInfo clearPreferredLanguages]
+ -[NTPBUserInfo copyWithZone:]
+ -[NTPBUserInfo description]
+ -[NTPBUserInfo dictionaryRepresentation]
+ -[NTPBUserInfo hasStorefrontId]
+ -[NTPBUserInfo hasSubscriberType]
+ -[NTPBUserInfo hash]
+ -[NTPBUserInfo isEqual:]
+ -[NTPBUserInfo mergeFrom:]
+ -[NTPBUserInfo preferredLanguagesAtIndex:]
+ -[NTPBUserInfo preferredLanguagesCount]
+ -[NTPBUserInfo preferredLanguages]
+ -[NTPBUserInfo readFrom:]
+ -[NTPBUserInfo setHasSubscriberType:]
+ -[NTPBUserInfo setPreferredLanguages:]
+ -[NTPBUserInfo setStorefrontId:]
+ -[NTPBUserInfo setSubscriberType:]
+ -[NTPBUserInfo storefrontId]
+ -[NTPBUserInfo subscriberType]
+ -[NTPBUserInfo writeTo:]
+ OBJC_IVAR_$_NTPBArticleRecord._recipeIDs
+ OBJC_IVAR_$_NTPBArticleTopic._isEligibleForFoodGrouping
+ OBJC_IVAR_$_NTPBArticleTopic._isEligibleForFoodGroupingIfAutofavorited
+ OBJC_IVAR_$_NTPBArticleTopic._isEligibleForFoodGroupingIfFavorited
+ OBJC_IVAR_$_NTPBCKConfiguration._created
+ OBJC_IVAR_$_NTPBCKConfiguration._expires
+ OBJC_IVAR_$_NTPBCKConfiguration._fields
+ OBJC_IVAR_$_NTPBCKConfiguration._has
+ OBJC_IVAR_$_NTPBCKConfigurationField._name
+ OBJC_IVAR_$_NTPBCKConfigurationField._value
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._boolValue
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._bytesValue
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._doubleValue
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._fieldValues
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._has
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._listValues
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._longValue
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._stringValue
+ OBJC_IVAR_$_NTPBCKConfigurationFieldValue._type
+ OBJC_IVAR_$_NTPBCKDate._has
+ OBJC_IVAR_$_NTPBCKDate._time
+ OBJC_IVAR_$_NTPBCKDateStatistics._creation
+ OBJC_IVAR_$_NTPBCKDateStatistics._modification
+ OBJC_IVAR_$_NTPBCKIdentifier._has
+ OBJC_IVAR_$_NTPBCKIdentifier._name
+ OBJC_IVAR_$_NTPBCKIdentifier._type
+ OBJC_IVAR_$_NTPBCKLocale._activeKeyboard
+ OBJC_IVAR_$_NTPBCKLocale._enabledKeyboards
+ OBJC_IVAR_$_NTPBCKLocale._languageCode
+ OBJC_IVAR_$_NTPBCKLocale._regionCode
+ OBJC_IVAR_$_NTPBCKOperation._has
+ OBJC_IVAR_$_NTPBCKOperation._last
+ OBJC_IVAR_$_NTPBCKOperation._operationUUID
+ OBJC_IVAR_$_NTPBCKOperation._synchronousMode
+ OBJC_IVAR_$_NTPBCKOperation._type
+ OBJC_IVAR_$_NTPBCKQuery._distinct
+ OBJC_IVAR_$_NTPBCKQuery._filters
+ OBJC_IVAR_$_NTPBCKQuery._has
+ OBJC_IVAR_$_NTPBCKQuery._queryOperator
+ OBJC_IVAR_$_NTPBCKQuery._sorts
+ OBJC_IVAR_$_NTPBCKQuery._types
+ OBJC_IVAR_$_NTPBCKQueryFilter._fieldName
+ OBJC_IVAR_$_NTPBCKQueryFilter._fieldValue
+ OBJC_IVAR_$_NTPBCKQueryFilter._has
+ OBJC_IVAR_$_NTPBCKQueryFilter._type
+ OBJC_IVAR_$_NTPBCKQueryRetrieveRequest._continuationMarker
+ OBJC_IVAR_$_NTPBCKQueryRetrieveRequest._has
+ OBJC_IVAR_$_NTPBCKQueryRetrieveRequest._limit
+ OBJC_IVAR_$_NTPBCKQueryRetrieveRequest._query
+ OBJC_IVAR_$_NTPBCKQueryRetrieveRequest._requestedFields
+ OBJC_IVAR_$_NTPBCKQueryRetrieveRequest._zoneIdentifier
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponse._continuationMarker
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponse._queryResults
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponseQueryResult._etag
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponseQueryResult._has
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponseQueryResult._identifier
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponseQueryResult._record
+ OBJC_IVAR_$_NTPBCKQueryRetrieveResponseQueryResult._type
+ OBJC_IVAR_$_NTPBCKQuerySort._fieldName
+ OBJC_IVAR_$_NTPBCKQuerySort._has
+ OBJC_IVAR_$_NTPBCKQuerySort._order
+ OBJC_IVAR_$_NTPBCKRecord._etag
+ OBJC_IVAR_$_NTPBCKRecord._fields
+ OBJC_IVAR_$_NTPBCKRecord._recordIdentifier
+ OBJC_IVAR_$_NTPBCKRecord._timeStatistics
+ OBJC_IVAR_$_NTPBCKRecord._type
+ OBJC_IVAR_$_NTPBCKRecordField._identifier
+ OBJC_IVAR_$_NTPBCKRecordField._value
+ OBJC_IVAR_$_NTPBCKRecordFieldIdentifier._name
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._bytesValue
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._dateValue
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._doubleValue
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._has
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._listValues
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._referenceValue
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._signedValue
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._stringValue
+ OBJC_IVAR_$_NTPBCKRecordFieldValue._type
+ OBJC_IVAR_$_NTPBCKRecordIdentifier._value
+ OBJC_IVAR_$_NTPBCKRecordIdentifier._zoneIdentifier
+ OBJC_IVAR_$_NTPBCKRecordReference._has
+ OBJC_IVAR_$_NTPBCKRecordReference._recordIdentifier
+ OBJC_IVAR_$_NTPBCKRecordReference._type
+ OBJC_IVAR_$_NTPBCKRecordRetrieveRequest._clientVersionETag
+ OBJC_IVAR_$_NTPBCKRecordRetrieveRequest._recordIdentifier
+ OBJC_IVAR_$_NTPBCKRecordRetrieveRequest._requestedFields
+ OBJC_IVAR_$_NTPBCKRecordRetrieveRequest._versionETag
+ OBJC_IVAR_$_NTPBCKRecordRetrieveResponse._record
+ OBJC_IVAR_$_NTPBCKRecordType._name
+ OBJC_IVAR_$_NTPBCKRecordZoneIdentifier._ownerIdentifier
+ OBJC_IVAR_$_NTPBCKRecordZoneIdentifier._value
+ OBJC_IVAR_$_NTPBCKRequestOperation._header
+ OBJC_IVAR_$_NTPBCKRequestOperation._queryRetrieveRequest
+ OBJC_IVAR_$_NTPBCKRequestOperation._recordRetrieveRequest
+ OBJC_IVAR_$_NTPBCKRequestOperation._request
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._applicationBundle
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._applicationConfigVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._applicationContainer
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._applicationContainerEnvironment
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._applicationVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._clientChangeToken
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceAssignedName
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceFlowControlBudget
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceFlowControlBudgetCap
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceFlowControlKey
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceFlowControlRegeneration
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceHardwareID
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceHardwareVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceIdentifier
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceLibraryName
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceLibraryVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceProtocolVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceSoftwareIsAppleInternal
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._deviceSoftwareVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._globalConfigVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._has
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._isolationLevel
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._locale
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._mmcsProtocolVersion
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._operationGroupName
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._operationGroupQuantity
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._targetDatabase
+ OBJC_IVAR_$_NTPBCKRequestOperationHeader._userIDContainerID
+ OBJC_IVAR_$_NTPBCKRequestedFields._fields
+ OBJC_IVAR_$_NTPBCKResponseOperation._queryRetrieveResponse
+ OBJC_IVAR_$_NTPBCKResponseOperation._recordRetrieveResponse
+ OBJC_IVAR_$_NTPBCKResponseOperation._response
+ OBJC_IVAR_$_NTPBCKResponseOperation._result
+ OBJC_IVAR_$_NTPBCKResponseOperationResult._code
+ OBJC_IVAR_$_NTPBCKResponseOperationResult._error
+ OBJC_IVAR_$_NTPBCKResponseOperationResult._has
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._clientError
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._errorDescription
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._errorKey
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._extensionError
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._has
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._retryAfterSeconds
+ OBJC_IVAR_$_NTPBCKResponseOperationResultError._serverError
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorClient._has
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorClient._type
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorExtension._extensionName
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorExtension._extensionPayload
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorExtension._has
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorExtension._typeCode
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorServer._has
+ OBJC_IVAR_$_NTPBCKResponseOperationResultErrorServer._type
+ OBJC_IVAR_$_NTPBFeedItem._storyType
+ OBJC_IVAR_$_NTPBFeedItem._surfacedByChannelID
+ OBJC_IVAR_$_NTPBFeedItem._surfacedByFlags
+ OBJC_IVAR_$_NTPBFeedItem._surfacedBySectionID
+ OBJC_IVAR_$_NTPBFeedItem._surfacedByTopicID
+ OBJC_IVAR_$_NTPBFetchRecordSpec._desiredFields
+ OBJC_IVAR_$_NTPBFetchRecordSpec._linkedFields
+ OBJC_IVAR_$_NTPBFetchRecordSpec._recordType
+ OBJC_IVAR_$_NTPBForYouTodaySectionSpecificConfig._feedItemMaxCount
+ OBJC_IVAR_$_NTPBNetworkEvent._smarterFetchSources
+ OBJC_IVAR_$_NTPBNetworkEvent._smarterFetchStrategy
+ OBJC_IVAR_$_NTPBPersonalizationParams._uivModelId
+ OBJC_IVAR_$_NTPBPersonalizationParams._userInterestVector
+ OBJC_IVAR_$_NTPBRecipeListRecord._base
+ OBJC_IVAR_$_NTPBRecipeListRecord._recipeIDs
+ OBJC_IVAR_$_NTPBRecipeRecord._allowedStorefrontIDs
+ OBJC_IVAR_$_NTPBRecipeRecord._articleIDs
+ OBJC_IVAR_$_NTPBRecipeRecord._authors
+ OBJC_IVAR_$_NTPBRecipeRecord._base
+ OBJC_IVAR_$_NTPBRecipeRecord._blockedStorefrontIDs
+ OBJC_IVAR_$_NTPBRecipeRecord._contentType
+ OBJC_IVAR_$_NTPBRecipeRecord._contentURL
+ OBJC_IVAR_$_NTPBRecipeRecord._eventAggregationPersonalizationData
+ OBJC_IVAR_$_NTPBRecipeRecord._has
+ OBJC_IVAR_$_NTPBRecipeRecord._iAdCategories
+ OBJC_IVAR_$_NTPBRecipeRecord._iAdKeywords
+ OBJC_IVAR_$_NTPBRecipeRecord._iAdSectionTagIDs
+ OBJC_IVAR_$_NTPBRecipeRecord._isDraft
+ OBJC_IVAR_$_NTPBRecipeRecord._isPaid
+ OBJC_IVAR_$_NTPBRecipeRecord._language
+ OBJC_IVAR_$_NTPBRecipeRecord._lastReferenceDate
+ OBJC_IVAR_$_NTPBRecipeRecord._minimumNewsVersion
+ OBJC_IVAR_$_NTPBRecipeRecord._personalizationData
+ OBJC_IVAR_$_NTPBRecipeRecord._publishDate
+ OBJC_IVAR_$_NTPBRecipeRecord._rapidUpdatePersonalizationData
+ OBJC_IVAR_$_NTPBRecipeRecord._recipesRecirculationDataURL
+ OBJC_IVAR_$_NTPBRecipeRecord._shortExcerpt
+ OBJC_IVAR_$_NTPBRecipeRecord._sourceChannelTagID
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailAccentColor
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailBackgroundColor
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailExtraLargeMetadata
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailExtraLargeURL
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailFocalFrame
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailLargeMetadata
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailLargeURL
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailMediumMetadata
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailMediumURL
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailPerceptualHash
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailPrimaryColor
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailSmallMetadata
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailSmallURL
+ OBJC_IVAR_$_NTPBRecipeRecord._thumbnailTextColor
+ OBJC_IVAR_$_NTPBRecipeRecord._title
+ OBJC_IVAR_$_NTPBRecipeRecord._topicTagIDs
+ OBJC_IVAR_$_NTPBRecipeRecord._topics
+ OBJC_IVAR_$_NTPBRecipeRecord._totalTime
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._personalizationParams
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._tagsFolloweds
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._todayFeedPoolRequests
+ OBJC_IVAR_$_NTPBSmarterFetchRequest._userInfo
+ OBJC_IVAR_$_NTPBSmarterFetchResponse._todayFeedPoolResponses
+ OBJC_IVAR_$_NTPBTagFollowed._aLaCarteSubscribed
+ OBJC_IVAR_$_NTPBTagFollowed._has
+ OBJC_IVAR_$_NTPBTagFollowed._tagFollowMode
+ OBJC_IVAR_$_NTPBTagFollowed._tagId
+ OBJC_IVAR_$_NTPBTagRecord._foodGroupingAvailability
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fetchRecordSpecs
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fetchSource
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fetchStrategy
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._fromTimestamp
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._has
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._previousFromTimestamp
+ OBJC_IVAR_$_NTPBTodayFeedPoolRequest._requestId
+ OBJC_IVAR_$_NTPBTodayFeedPoolResponse._has
+ OBJC_IVAR_$_NTPBTodayFeedPoolResponse._nextFromTimestamp
+ OBJC_IVAR_$_NTPBTodayFeedPoolResponse._records
+ OBJC_IVAR_$_NTPBTodayFeedPoolResponse._requestId
+ OBJC_IVAR_$_NTPBTodayFeedPoolResponse._ttlSecs
+ OBJC_IVAR_$_NTPBUserInfo._has
+ OBJC_IVAR_$_NTPBUserInfo._preferredLanguages
+ OBJC_IVAR_$_NTPBUserInfo._storefrontId
+ OBJC_IVAR_$_NTPBUserInfo._subscriberType
+ _NTPBCKConfigurationFieldReadFrom
+ _NTPBCKConfigurationFieldValueReadFrom
+ _NTPBCKConfigurationReadFrom
+ _NTPBCKDateReadFrom
+ _NTPBCKDateStatisticsReadFrom
+ _NTPBCKIdentifierReadFrom
+ _NTPBCKLocaleReadFrom
+ _NTPBCKOperationReadFrom
+ _NTPBCKQueryFilterReadFrom
+ _NTPBCKQueryReadFrom
+ _NTPBCKQueryRetrieveRequestReadFrom
+ _NTPBCKQueryRetrieveResponseQueryResultReadFrom
+ _NTPBCKQueryRetrieveResponseReadFrom
+ _NTPBCKQuerySortReadFrom
+ _NTPBCKRecordFieldIdentifierReadFrom
+ _NTPBCKRecordFieldReadFrom
+ _NTPBCKRecordFieldValueReadFrom
+ _NTPBCKRecordIdentifierReadFrom
+ _NTPBCKRecordReadFrom
+ _NTPBCKRecordReferenceReadFrom
+ _NTPBCKRecordRetrieveRequestReadFrom
+ _NTPBCKRecordRetrieveResponseReadFrom
+ _NTPBCKRecordTypeReadFrom
+ _NTPBCKRecordZoneIdentifierReadFrom
+ _NTPBCKRequestOperationHeaderReadFrom
+ _NTPBCKRequestOperationReadFrom
+ _NTPBCKRequestedFieldsReadFrom
+ _NTPBCKResponseOperationReadFrom
+ _NTPBCKResponseOperationResultErrorClientReadFrom
+ _NTPBCKResponseOperationResultErrorExtensionReadFrom
+ _NTPBCKResponseOperationResultErrorReadFrom
+ _NTPBCKResponseOperationResultErrorServerReadFrom
+ _NTPBCKResponseOperationResultReadFrom
+ _NTPBFetchRecordSpecReadFrom
+ _NTPBPersonalizationParamsReadFrom
+ _NTPBRecipeListRecordReadFrom
+ _NTPBRecipeRecordReadFrom
+ _NTPBSmarterFetchRequestReadFrom
+ _NTPBSmarterFetchResponseReadFrom
+ _NTPBTagFollowedReadFrom
+ _NTPBTodayFeedPoolRequestReadFrom
+ _NTPBTodayFeedPoolResponseReadFrom
+ _NTPBUserInfoReadFrom
+ _OBJC_CLASS_$_NTPBCKConfiguration
+ _OBJC_CLASS_$_NTPBCKConfigurationField
+ _OBJC_CLASS_$_NTPBCKConfigurationFieldValue
+ _OBJC_CLASS_$_NTPBCKDate
+ _OBJC_CLASS_$_NTPBCKDateStatistics
+ _OBJC_CLASS_$_NTPBCKIdentifier
+ _OBJC_CLASS_$_NTPBCKLocale
+ _OBJC_CLASS_$_NTPBCKOperation
+ _OBJC_CLASS_$_NTPBCKQuery
+ _OBJC_CLASS_$_NTPBCKQueryFilter
+ _OBJC_CLASS_$_NTPBCKQueryRetrieveRequest
+ _OBJC_CLASS_$_NTPBCKQueryRetrieveResponse
+ _OBJC_CLASS_$_NTPBCKQueryRetrieveResponseQueryResult
+ _OBJC_CLASS_$_NTPBCKQuerySort
+ _OBJC_CLASS_$_NTPBCKRecord
+ _OBJC_CLASS_$_NTPBCKRecordField
+ _OBJC_CLASS_$_NTPBCKRecordFieldIdentifier
+ _OBJC_CLASS_$_NTPBCKRecordFieldValue
+ _OBJC_CLASS_$_NTPBCKRecordIdentifier
+ _OBJC_CLASS_$_NTPBCKRecordReference
+ _OBJC_CLASS_$_NTPBCKRecordRetrieveRequest
+ _OBJC_CLASS_$_NTPBCKRecordRetrieveResponse
+ _OBJC_CLASS_$_NTPBCKRecordType
+ _OBJC_CLASS_$_NTPBCKRecordZoneIdentifier
+ _OBJC_CLASS_$_NTPBCKRequestOperation
+ _OBJC_CLASS_$_NTPBCKRequestOperationHeader
+ _OBJC_CLASS_$_NTPBCKRequestedFields
+ _OBJC_CLASS_$_NTPBCKResponseOperation
+ _OBJC_CLASS_$_NTPBCKResponseOperationResult
+ _OBJC_CLASS_$_NTPBCKResponseOperationResultError
+ _OBJC_CLASS_$_NTPBCKResponseOperationResultErrorClient
+ _OBJC_CLASS_$_NTPBCKResponseOperationResultErrorExtension
+ _OBJC_CLASS_$_NTPBCKResponseOperationResultErrorServer
+ _OBJC_CLASS_$_NTPBFetchRecordSpec
+ _OBJC_CLASS_$_NTPBPersonalizationParams
+ _OBJC_CLASS_$_NTPBRecipeListRecord
+ _OBJC_CLASS_$_NTPBRecipeRecord
+ _OBJC_CLASS_$_NTPBSmarterFetchRequest
+ _OBJC_CLASS_$_NTPBSmarterFetchResponse
+ _OBJC_CLASS_$_NTPBTagFollowed
+ _OBJC_CLASS_$_NTPBTodayFeedPoolRequest
+ _OBJC_CLASS_$_NTPBTodayFeedPoolResponse
+ _OBJC_CLASS_$_NTPBUserInfo
+ _OBJC_METACLASS_$_NTPBCKConfiguration
+ _OBJC_METACLASS_$_NTPBCKConfigurationField
+ _OBJC_METACLASS_$_NTPBCKConfigurationFieldValue
+ _OBJC_METACLASS_$_NTPBCKDate
+ _OBJC_METACLASS_$_NTPBCKDateStatistics
+ _OBJC_METACLASS_$_NTPBCKIdentifier
+ _OBJC_METACLASS_$_NTPBCKLocale
+ _OBJC_METACLASS_$_NTPBCKOperation
+ _OBJC_METACLASS_$_NTPBCKQuery
+ _OBJC_METACLASS_$_NTPBCKQueryFilter
+ _OBJC_METACLASS_$_NTPBCKQueryRetrieveRequest
+ _OBJC_METACLASS_$_NTPBCKQueryRetrieveResponse
+ _OBJC_METACLASS_$_NTPBCKQueryRetrieveResponseQueryResult
+ _OBJC_METACLASS_$_NTPBCKQuerySort
+ _OBJC_METACLASS_$_NTPBCKRecord
+ _OBJC_METACLASS_$_NTPBCKRecordField
+ _OBJC_METACLASS_$_NTPBCKRecordFieldIdentifier
+ _OBJC_METACLASS_$_NTPBCKRecordFieldValue
+ _OBJC_METACLASS_$_NTPBCKRecordIdentifier
+ _OBJC_METACLASS_$_NTPBCKRecordReference
+ _OBJC_METACLASS_$_NTPBCKRecordRetrieveRequest
+ _OBJC_METACLASS_$_NTPBCKRecordRetrieveResponse
+ _OBJC_METACLASS_$_NTPBCKRecordType
+ _OBJC_METACLASS_$_NTPBCKRecordZoneIdentifier
+ _OBJC_METACLASS_$_NTPBCKRequestOperation
+ _OBJC_METACLASS_$_NTPBCKRequestOperationHeader
+ _OBJC_METACLASS_$_NTPBCKRequestedFields
+ _OBJC_METACLASS_$_NTPBCKResponseOperation
+ _OBJC_METACLASS_$_NTPBCKResponseOperationResult
+ _OBJC_METACLASS_$_NTPBCKResponseOperationResultError
+ _OBJC_METACLASS_$_NTPBCKResponseOperationResultErrorClient
+ _OBJC_METACLASS_$_NTPBCKResponseOperationResultErrorExtension
+ _OBJC_METACLASS_$_NTPBCKResponseOperationResultErrorServer
+ _OBJC_METACLASS_$_NTPBFetchRecordSpec
+ _OBJC_METACLASS_$_NTPBPersonalizationParams
+ _OBJC_METACLASS_$_NTPBRecipeListRecord
+ _OBJC_METACLASS_$_NTPBRecipeRecord
+ _OBJC_METACLASS_$_NTPBSmarterFetchRequest
+ _OBJC_METACLASS_$_NTPBSmarterFetchResponse
+ _OBJC_METACLASS_$_NTPBTagFollowed
+ _OBJC_METACLASS_$_NTPBTodayFeedPoolRequest
+ _OBJC_METACLASS_$_NTPBTodayFeedPoolResponse
+ _OBJC_METACLASS_$_NTPBUserInfo
+ __OBJC_$_CLASS_METHODS_NTPBCKConfiguration
+ __OBJC_$_CLASS_METHODS_NTPBCKConfigurationFieldValue
+ __OBJC_$_CLASS_METHODS_NTPBCKLocale
+ __OBJC_$_CLASS_METHODS_NTPBCKQuery
+ __OBJC_$_CLASS_METHODS_NTPBCKQueryRetrieveResponse
+ __OBJC_$_CLASS_METHODS_NTPBCKRecord
+ __OBJC_$_CLASS_METHODS_NTPBCKRecordFieldValue
+ __OBJC_$_CLASS_METHODS_NTPBCKRequestedFields
+ __OBJC_$_CLASS_METHODS_NTPBFetchRecordSpec
+ __OBJC_$_CLASS_METHODS_NTPBNetworkEvent
+ __OBJC_$_CLASS_METHODS_NTPBRecipeListRecord
+ __OBJC_$_CLASS_METHODS_NTPBRecipeRecord
+ __OBJC_$_CLASS_METHODS_NTPBSmarterFetchRequest
+ __OBJC_$_CLASS_METHODS_NTPBSmarterFetchResponse
+ __OBJC_$_CLASS_METHODS_NTPBTodayFeedPoolRequest
+ __OBJC_$_CLASS_METHODS_NTPBTodayFeedPoolResponse
+ __OBJC_$_CLASS_METHODS_NTPBUserInfo
+ __OBJC_$_INSTANCE_METHODS_NTPBCKConfiguration
+ __OBJC_$_INSTANCE_METHODS_NTPBCKConfigurationField
+ __OBJC_$_INSTANCE_METHODS_NTPBCKConfigurationFieldValue
+ __OBJC_$_INSTANCE_METHODS_NTPBCKDate
+ __OBJC_$_INSTANCE_METHODS_NTPBCKDateStatistics
+ __OBJC_$_INSTANCE_METHODS_NTPBCKIdentifier
+ __OBJC_$_INSTANCE_METHODS_NTPBCKLocale
+ __OBJC_$_INSTANCE_METHODS_NTPBCKOperation
+ __OBJC_$_INSTANCE_METHODS_NTPBCKQuery
+ __OBJC_$_INSTANCE_METHODS_NTPBCKQueryFilter
+ __OBJC_$_INSTANCE_METHODS_NTPBCKQueryRetrieveRequest
+ __OBJC_$_INSTANCE_METHODS_NTPBCKQueryRetrieveResponse
+ __OBJC_$_INSTANCE_METHODS_NTPBCKQueryRetrieveResponseQueryResult
+ __OBJC_$_INSTANCE_METHODS_NTPBCKQuerySort
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecord
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordField
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordFieldIdentifier
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordFieldValue
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordIdentifier
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordReference
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordRetrieveRequest
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordRetrieveResponse
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordType
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRecordZoneIdentifier
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRequestOperation
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRequestOperationHeader
+ __OBJC_$_INSTANCE_METHODS_NTPBCKRequestedFields
+ __OBJC_$_INSTANCE_METHODS_NTPBCKResponseOperation
+ __OBJC_$_INSTANCE_METHODS_NTPBCKResponseOperationResult
+ __OBJC_$_INSTANCE_METHODS_NTPBCKResponseOperationResultError
+ __OBJC_$_INSTANCE_METHODS_NTPBCKResponseOperationResultErrorClient
+ __OBJC_$_INSTANCE_METHODS_NTPBCKResponseOperationResultErrorExtension
+ __OBJC_$_INSTANCE_METHODS_NTPBCKResponseOperationResultErrorServer
+ __OBJC_$_INSTANCE_METHODS_NTPBFetchRecordSpec
+ __OBJC_$_INSTANCE_METHODS_NTPBPersonalizationParams
+ __OBJC_$_INSTANCE_METHODS_NTPBRecipeListRecord
+ __OBJC_$_INSTANCE_METHODS_NTPBRecipeRecord
+ __OBJC_$_INSTANCE_METHODS_NTPBSmarterFetchRequest
+ __OBJC_$_INSTANCE_METHODS_NTPBSmarterFetchResponse
+ __OBJC_$_INSTANCE_METHODS_NTPBTagFollowed
+ __OBJC_$_INSTANCE_METHODS_NTPBTodayFeedPoolRequest
+ __OBJC_$_INSTANCE_METHODS_NTPBTodayFeedPoolResponse
+ __OBJC_$_INSTANCE_METHODS_NTPBUserInfo
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKConfigurationField
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKConfigurationFieldValue
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKDate
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKDateStatistics
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKLocale
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKOperation
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKQuery
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKQueryFilter
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKQueryRetrieveRequest
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKQueryRetrieveResponse
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKQueryRetrieveResponseQueryResult
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKQuerySort
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecord
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordField
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordFieldIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordFieldValue
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordReference
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordRetrieveRequest
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordRetrieveResponse
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordType
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRecordZoneIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRequestOperation
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRequestOperationHeader
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKRequestedFields
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKResponseOperation
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKResponseOperationResult
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKResponseOperationResultError
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKResponseOperationResultErrorClient
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKResponseOperationResultErrorExtension
+ __OBJC_$_INSTANCE_VARIABLES_NTPBCKResponseOperationResultErrorServer
+ __OBJC_$_INSTANCE_VARIABLES_NTPBFetchRecordSpec
+ __OBJC_$_INSTANCE_VARIABLES_NTPBPersonalizationParams
+ __OBJC_$_INSTANCE_VARIABLES_NTPBRecipeListRecord
+ __OBJC_$_INSTANCE_VARIABLES_NTPBRecipeRecord
+ __OBJC_$_INSTANCE_VARIABLES_NTPBSmarterFetchRequest
+ __OBJC_$_INSTANCE_VARIABLES_NTPBSmarterFetchResponse
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTagFollowed
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTodayFeedPoolRequest
+ __OBJC_$_INSTANCE_VARIABLES_NTPBTodayFeedPoolResponse
+ __OBJC_$_INSTANCE_VARIABLES_NTPBUserInfo
+ __OBJC_$_PROP_LIST_NTPBCKConfiguration
+ __OBJC_$_PROP_LIST_NTPBCKConfigurationField
+ __OBJC_$_PROP_LIST_NTPBCKConfigurationFieldValue
+ __OBJC_$_PROP_LIST_NTPBCKDate
+ __OBJC_$_PROP_LIST_NTPBCKDateStatistics
+ __OBJC_$_PROP_LIST_NTPBCKIdentifier
+ __OBJC_$_PROP_LIST_NTPBCKLocale
+ __OBJC_$_PROP_LIST_NTPBCKOperation
+ __OBJC_$_PROP_LIST_NTPBCKQuery
+ __OBJC_$_PROP_LIST_NTPBCKQueryFilter
+ __OBJC_$_PROP_LIST_NTPBCKQueryRetrieveRequest
+ __OBJC_$_PROP_LIST_NTPBCKQueryRetrieveResponse
+ __OBJC_$_PROP_LIST_NTPBCKQueryRetrieveResponseQueryResult
+ __OBJC_$_PROP_LIST_NTPBCKQuerySort
+ __OBJC_$_PROP_LIST_NTPBCKRecord
+ __OBJC_$_PROP_LIST_NTPBCKRecordField
+ __OBJC_$_PROP_LIST_NTPBCKRecordFieldIdentifier
+ __OBJC_$_PROP_LIST_NTPBCKRecordFieldValue
+ __OBJC_$_PROP_LIST_NTPBCKRecordIdentifier
+ __OBJC_$_PROP_LIST_NTPBCKRecordReference
+ __OBJC_$_PROP_LIST_NTPBCKRecordRetrieveRequest
+ __OBJC_$_PROP_LIST_NTPBCKRecordRetrieveResponse
+ __OBJC_$_PROP_LIST_NTPBCKRecordType
+ __OBJC_$_PROP_LIST_NTPBCKRecordZoneIdentifier
+ __OBJC_$_PROP_LIST_NTPBCKRequestOperation
+ __OBJC_$_PROP_LIST_NTPBCKRequestOperationHeader
+ __OBJC_$_PROP_LIST_NTPBCKRequestedFields
+ __OBJC_$_PROP_LIST_NTPBCKResponseOperation
+ __OBJC_$_PROP_LIST_NTPBCKResponseOperationResult
+ __OBJC_$_PROP_LIST_NTPBCKResponseOperationResultError
+ __OBJC_$_PROP_LIST_NTPBCKResponseOperationResultErrorClient
+ __OBJC_$_PROP_LIST_NTPBCKResponseOperationResultErrorExtension
+ __OBJC_$_PROP_LIST_NTPBCKResponseOperationResultErrorServer
+ __OBJC_$_PROP_LIST_NTPBFetchRecordSpec
+ __OBJC_$_PROP_LIST_NTPBPersonalizationParams
+ __OBJC_$_PROP_LIST_NTPBRecipeListRecord
+ __OBJC_$_PROP_LIST_NTPBRecipeRecord
+ __OBJC_$_PROP_LIST_NTPBSmarterFetchRequest
+ __OBJC_$_PROP_LIST_NTPBSmarterFetchResponse
+ __OBJC_$_PROP_LIST_NTPBTagFollowed
+ __OBJC_$_PROP_LIST_NTPBTodayFeedPoolRequest
+ __OBJC_$_PROP_LIST_NTPBTodayFeedPoolResponse
+ __OBJC_$_PROP_LIST_NTPBUserInfo
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKConfigurationField
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKConfigurationFieldValue
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKDate
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKDateStatistics
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKLocale
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKOperation
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKQuery
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKQueryFilter
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKQueryRetrieveRequest
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKQueryRetrieveResponse
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKQueryRetrieveResponseQueryResult
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKQuerySort
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecord
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordField
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordFieldIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordFieldValue
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordReference
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordRetrieveRequest
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordRetrieveResponse
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordType
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRecordZoneIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRequestOperation
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRequestOperationHeader
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKRequestedFields
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKResponseOperation
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKResponseOperationResult
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKResponseOperationResultError
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKResponseOperationResultErrorClient
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKResponseOperationResultErrorExtension
+ __OBJC_CLASS_PROTOCOLS_$_NTPBCKResponseOperationResultErrorServer
+ __OBJC_CLASS_PROTOCOLS_$_NTPBFetchRecordSpec
+ __OBJC_CLASS_PROTOCOLS_$_NTPBPersonalizationParams
+ __OBJC_CLASS_PROTOCOLS_$_NTPBRecipeListRecord
+ __OBJC_CLASS_PROTOCOLS_$_NTPBRecipeRecord
+ __OBJC_CLASS_PROTOCOLS_$_NTPBSmarterFetchRequest
+ __OBJC_CLASS_PROTOCOLS_$_NTPBSmarterFetchResponse
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTagFollowed
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTodayFeedPoolRequest
+ __OBJC_CLASS_PROTOCOLS_$_NTPBTodayFeedPoolResponse
+ __OBJC_CLASS_PROTOCOLS_$_NTPBUserInfo
+ __OBJC_CLASS_RO_$_NTPBCKConfiguration
+ __OBJC_CLASS_RO_$_NTPBCKConfigurationField
+ __OBJC_CLASS_RO_$_NTPBCKConfigurationFieldValue
+ __OBJC_CLASS_RO_$_NTPBCKDate
+ __OBJC_CLASS_RO_$_NTPBCKDateStatistics
+ __OBJC_CLASS_RO_$_NTPBCKIdentifier
+ __OBJC_CLASS_RO_$_NTPBCKLocale
+ __OBJC_CLASS_RO_$_NTPBCKOperation
+ __OBJC_CLASS_RO_$_NTPBCKQuery
+ __OBJC_CLASS_RO_$_NTPBCKQueryFilter
+ __OBJC_CLASS_RO_$_NTPBCKQueryRetrieveRequest
+ __OBJC_CLASS_RO_$_NTPBCKQueryRetrieveResponse
+ __OBJC_CLASS_RO_$_NTPBCKQueryRetrieveResponseQueryResult
+ __OBJC_CLASS_RO_$_NTPBCKQuerySort
+ __OBJC_CLASS_RO_$_NTPBCKRecord
+ __OBJC_CLASS_RO_$_NTPBCKRecordField
+ __OBJC_CLASS_RO_$_NTPBCKRecordFieldIdentifier
+ __OBJC_CLASS_RO_$_NTPBCKRecordFieldValue
+ __OBJC_CLASS_RO_$_NTPBCKRecordIdentifier
+ __OBJC_CLASS_RO_$_NTPBCKRecordReference
+ __OBJC_CLASS_RO_$_NTPBCKRecordRetrieveRequest
+ __OBJC_CLASS_RO_$_NTPBCKRecordRetrieveResponse
+ __OBJC_CLASS_RO_$_NTPBCKRecordType
+ __OBJC_CLASS_RO_$_NTPBCKRecordZoneIdentifier
+ __OBJC_CLASS_RO_$_NTPBCKRequestOperation
+ __OBJC_CLASS_RO_$_NTPBCKRequestOperationHeader
+ __OBJC_CLASS_RO_$_NTPBCKRequestedFields
+ __OBJC_CLASS_RO_$_NTPBCKResponseOperation
+ __OBJC_CLASS_RO_$_NTPBCKResponseOperationResult
+ __OBJC_CLASS_RO_$_NTPBCKResponseOperationResultError
+ __OBJC_CLASS_RO_$_NTPBCKResponseOperationResultErrorClient
+ __OBJC_CLASS_RO_$_NTPBCKResponseOperationResultErrorExtension
+ __OBJC_CLASS_RO_$_NTPBCKResponseOperationResultErrorServer
+ __OBJC_CLASS_RO_$_NTPBFetchRecordSpec
+ __OBJC_CLASS_RO_$_NTPBPersonalizationParams
+ __OBJC_CLASS_RO_$_NTPBRecipeListRecord
+ __OBJC_CLASS_RO_$_NTPBRecipeRecord
+ __OBJC_CLASS_RO_$_NTPBSmarterFetchRequest
+ __OBJC_CLASS_RO_$_NTPBSmarterFetchResponse
+ __OBJC_CLASS_RO_$_NTPBTagFollowed
+ __OBJC_CLASS_RO_$_NTPBTodayFeedPoolRequest
+ __OBJC_CLASS_RO_$_NTPBTodayFeedPoolResponse
+ __OBJC_CLASS_RO_$_NTPBUserInfo
+ __OBJC_METACLASS_RO_$_NTPBCKConfiguration
+ __OBJC_METACLASS_RO_$_NTPBCKConfigurationField
+ __OBJC_METACLASS_RO_$_NTPBCKConfigurationFieldValue
+ __OBJC_METACLASS_RO_$_NTPBCKDate
+ __OBJC_METACLASS_RO_$_NTPBCKDateStatistics
+ __OBJC_METACLASS_RO_$_NTPBCKIdentifier
+ __OBJC_METACLASS_RO_$_NTPBCKLocale
+ __OBJC_METACLASS_RO_$_NTPBCKOperation
+ __OBJC_METACLASS_RO_$_NTPBCKQuery
+ __OBJC_METACLASS_RO_$_NTPBCKQueryFilter
+ __OBJC_METACLASS_RO_$_NTPBCKQueryRetrieveRequest
+ __OBJC_METACLASS_RO_$_NTPBCKQueryRetrieveResponse
+ __OBJC_METACLASS_RO_$_NTPBCKQueryRetrieveResponseQueryResult
+ __OBJC_METACLASS_RO_$_NTPBCKQuerySort
+ __OBJC_METACLASS_RO_$_NTPBCKRecord
+ __OBJC_METACLASS_RO_$_NTPBCKRecordField
+ __OBJC_METACLASS_RO_$_NTPBCKRecordFieldIdentifier
+ __OBJC_METACLASS_RO_$_NTPBCKRecordFieldValue
+ __OBJC_METACLASS_RO_$_NTPBCKRecordIdentifier
+ __OBJC_METACLASS_RO_$_NTPBCKRecordReference
+ __OBJC_METACLASS_RO_$_NTPBCKRecordRetrieveRequest
+ __OBJC_METACLASS_RO_$_NTPBCKRecordRetrieveResponse
+ __OBJC_METACLASS_RO_$_NTPBCKRecordType
+ __OBJC_METACLASS_RO_$_NTPBCKRecordZoneIdentifier
+ __OBJC_METACLASS_RO_$_NTPBCKRequestOperation
+ __OBJC_METACLASS_RO_$_NTPBCKRequestOperationHeader
+ __OBJC_METACLASS_RO_$_NTPBCKRequestedFields
+ __OBJC_METACLASS_RO_$_NTPBCKResponseOperation
+ __OBJC_METACLASS_RO_$_NTPBCKResponseOperationResult
+ __OBJC_METACLASS_RO_$_NTPBCKResponseOperationResultError
+ __OBJC_METACLASS_RO_$_NTPBCKResponseOperationResultErrorClient
+ __OBJC_METACLASS_RO_$_NTPBCKResponseOperationResultErrorExtension
+ __OBJC_METACLASS_RO_$_NTPBCKResponseOperationResultErrorServer
+ __OBJC_METACLASS_RO_$_NTPBFetchRecordSpec
+ __OBJC_METACLASS_RO_$_NTPBPersonalizationParams
+ __OBJC_METACLASS_RO_$_NTPBRecipeListRecord
+ __OBJC_METACLASS_RO_$_NTPBRecipeRecord
+ __OBJC_METACLASS_RO_$_NTPBSmarterFetchRequest
+ __OBJC_METACLASS_RO_$_NTPBSmarterFetchResponse
+ __OBJC_METACLASS_RO_$_NTPBTagFollowed
+ __OBJC_METACLASS_RO_$_NTPBTodayFeedPoolRequest
+ __OBJC_METACLASS_RO_$_NTPBTodayFeedPoolResponse
+ __OBJC_METACLASS_RO_$_NTPBUserInfo
+ _objc_msgSend$addDesiredFields:
+ _objc_msgSend$addEnabledKeyboards:
+ _objc_msgSend$addFetchRecordSpecs:
+ _objc_msgSend$addFieldValues:
+ _objc_msgSend$addFields:
+ _objc_msgSend$addFilters:
+ _objc_msgSend$addIAdSectionTagIDs:
+ _objc_msgSend$addLinkedFields:
+ _objc_msgSend$addListValue:
+ _objc_msgSend$addListValues:
+ _objc_msgSend$addPreferredLanguages:
+ _objc_msgSend$addQueryResults:
+ _objc_msgSend$addRecipeIDs:
+ _objc_msgSend$addRecords:
+ _objc_msgSend$addSmarterFetchSources:
+ _objc_msgSend$addSorts:
+ _objc_msgSend$addTagsFollowed:
+ _objc_msgSend$addTodayFeedPoolRequests:
+ _objc_msgSend$addTodayFeedPoolResponse:
+ _objc_msgSend$addTypes:
+ _objc_msgSend$setActiveKeyboard:
+ _objc_msgSend$setApplicationBundle:
+ _objc_msgSend$setApplicationContainer:
+ _objc_msgSend$setApplicationVersion:
+ _objc_msgSend$setBytesValue:
+ _objc_msgSend$setClientChangeToken:
+ _objc_msgSend$setClientError:
+ _objc_msgSend$setClientVersionETag:
+ _objc_msgSend$setContentType:
+ _objc_msgSend$setContinuationMarker:
+ _objc_msgSend$setCreation:
+ _objc_msgSend$setDeviceAssignedName:
+ _objc_msgSend$setDeviceFlowControlKey:
+ _objc_msgSend$setDeviceHardwareID:
+ _objc_msgSend$setDeviceHardwareVersion:
+ _objc_msgSend$setDeviceIdentifier:
+ _objc_msgSend$setDeviceLibraryName:
+ _objc_msgSend$setDeviceLibraryVersion:
+ _objc_msgSend$setDeviceSoftwareVersion:
+ _objc_msgSend$setError:
+ _objc_msgSend$setErrorDescription:
+ _objc_msgSend$setErrorKey:
+ _objc_msgSend$setEventAggregationPersonalizationData:
+ _objc_msgSend$setExtensionError:
+ _objc_msgSend$setExtensionName:
+ _objc_msgSend$setExtensionPayload:
+ _objc_msgSend$setFetchSource:
+ _objc_msgSend$setFetchStrategy:
+ _objc_msgSend$setFieldName:
+ _objc_msgSend$setFieldValue:
+ _objc_msgSend$setHeader:
+ _objc_msgSend$setIAdSectionTagIDs:
+ _objc_msgSend$setLastReferenceDate:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setMmcsProtocolVersion:
+ _objc_msgSend$setModification:
+ _objc_msgSend$setOperationGroupName:
+ _objc_msgSend$setOperationUUID:
+ _objc_msgSend$setOwnerIdentifier:
+ _objc_msgSend$setPersonalizationData:
+ _objc_msgSend$setPersonalizationParams:
+ _objc_msgSend$setQuery:
+ _objc_msgSend$setQueryRetrieveRequest:
+ _objc_msgSend$setQueryRetrieveResponse:
+ _objc_msgSend$setRapidUpdatePersonalizationData:
+ _objc_msgSend$setRecipeIDs:
+ _objc_msgSend$setRecipesRecirculationDataURL:
+ _objc_msgSend$setRecord:
+ _objc_msgSend$setRecordIdentifier:
+ _objc_msgSend$setRecordRetrieveRequest:
+ _objc_msgSend$setRecordRetrieveResponse:
+ _objc_msgSend$setRecordType:
+ _objc_msgSend$setReferenceValue:
+ _objc_msgSend$setRegionCode:
+ _objc_msgSend$setRequestId:
+ _objc_msgSend$setRequestedFields:
+ _objc_msgSend$setResponse:
+ _objc_msgSend$setResult:
+ _objc_msgSend$setServerError:
+ _objc_msgSend$setSmarterFetchSources:
+ _objc_msgSend$setSmarterFetchStrategy:
+ _objc_msgSend$setStorefrontId:
+ _objc_msgSend$setSurfacedByChannelID:
+ _objc_msgSend$setSurfacedBySectionID:
+ _objc_msgSend$setSurfacedByTopicID:
+ _objc_msgSend$setThumbnailExtraLargeURL:
+ _objc_msgSend$setThumbnailLargeURL:
+ _objc_msgSend$setThumbnailSmallURL:
+ _objc_msgSend$setTimeStatistics:
+ _objc_msgSend$setTotalTime:
+ _objc_msgSend$setUivModelId:
+ _objc_msgSend$setUserIDContainerID:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$setUserInterestVector:
+ _objc_msgSend$setVersionETag:
+ _objc_msgSend$setZoneIdentifier:
- -[NTPBAbsolutePersonalizedSectionPresenceConfig cTRToHide]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig cTRToShow]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig copyWithZone:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig description]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig dictionaryRepresentation]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig hasCTRToHide]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig hasCTRToShow]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig hasMinProbabilityToShow]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig hasSectionEdition]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig hash]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig isEqual:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig mergeFrom:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig minProbabilityToShow]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig readFrom:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig sectionEdition]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setCTRToHide:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setCTRToShow:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setHasCTRToHide:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setHasCTRToShow:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setHasMinProbabilityToShow:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setHasSectionEdition:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setMinProbabilityToShow:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig setSectionEdition:]
- -[NTPBAbsolutePersonalizedSectionPresenceConfig writeTo:]
- -[NTPBPersonalizedSectionPresenceConfig absoluteConfig]
- -[NTPBPersonalizedSectionPresenceConfig copyWithZone:]
- -[NTPBPersonalizedSectionPresenceConfig dealloc]
- -[NTPBPersonalizedSectionPresenceConfig description]
- -[NTPBPersonalizedSectionPresenceConfig dictionaryRepresentation]
- -[NTPBPersonalizedSectionPresenceConfig hasAbsoluteConfig]
- -[NTPBPersonalizedSectionPresenceConfig hasPersonalizationMethod]
- -[NTPBPersonalizedSectionPresenceConfig hasRelativeConfig]
- -[NTPBPersonalizedSectionPresenceConfig hash]
- -[NTPBPersonalizedSectionPresenceConfig isEqual:]
- -[NTPBPersonalizedSectionPresenceConfig mergeFrom:]
- -[NTPBPersonalizedSectionPresenceConfig personalizationMethod]
- -[NTPBPersonalizedSectionPresenceConfig readFrom:]
- -[NTPBPersonalizedSectionPresenceConfig relativeConfig]
- -[NTPBPersonalizedSectionPresenceConfig setAbsoluteConfig:]
- -[NTPBPersonalizedSectionPresenceConfig setHasPersonalizationMethod:]
- -[NTPBPersonalizedSectionPresenceConfig setPersonalizationMethod:]
- -[NTPBPersonalizedSectionPresenceConfig setRelativeConfig:]
- -[NTPBPersonalizedSectionPresenceConfig writeTo:]
- -[NTPBRelativePersonalizedSectionPresenceConfig copyWithZone:]
- -[NTPBRelativePersonalizedSectionPresenceConfig description]
- -[NTPBRelativePersonalizedSectionPresenceConfig dictionaryRepresentation]
- -[NTPBRelativePersonalizedSectionPresenceConfig hasScalar]
- -[NTPBRelativePersonalizedSectionPresenceConfig hash]
- -[NTPBRelativePersonalizedSectionPresenceConfig isEqual:]
- -[NTPBRelativePersonalizedSectionPresenceConfig mergeFrom:]
- -[NTPBRelativePersonalizedSectionPresenceConfig readFrom:]
- -[NTPBRelativePersonalizedSectionPresenceConfig scalar]
- -[NTPBRelativePersonalizedSectionPresenceConfig setHasScalar:]
- -[NTPBRelativePersonalizedSectionPresenceConfig setScalar:]
- -[NTPBRelativePersonalizedSectionPresenceConfig writeTo:]
- -[NTPBTodaySectionConfig hasPersonalizedPresenceConfig]
- -[NTPBTodaySectionConfig hasPersonalizedPresenceFeatureClickPrior]
- -[NTPBTodaySectionConfig hasPersonalizedPresenceFeatureID]
- -[NTPBTodaySectionConfig hasPersonalizedPresenceFeatureImpressionPrior]
- -[NTPBTodaySectionConfig hasPresenceDeterminedByPersonalization]
- -[NTPBTodaySectionConfig personalizedPresenceConfig]
- -[NTPBTodaySectionConfig personalizedPresenceFeatureClickPrior]
- -[NTPBTodaySectionConfig personalizedPresenceFeatureID]
- -[NTPBTodaySectionConfig personalizedPresenceFeatureImpressionPrior]
- -[NTPBTodaySectionConfig presenceDeterminedByPersonalization]
- -[NTPBTodaySectionConfig setHasPersonalizedPresenceFeatureClickPrior:]
- -[NTPBTodaySectionConfig setHasPersonalizedPresenceFeatureImpressionPrior:]
- -[NTPBTodaySectionConfig setHasPresenceDeterminedByPersonalization:]
- -[NTPBTodaySectionConfig setPersonalizedPresenceConfig:]
- -[NTPBTodaySectionConfig setPersonalizedPresenceFeatureClickPrior:]
- -[NTPBTodaySectionConfig setPersonalizedPresenceFeatureID:]
- -[NTPBTodaySectionConfig setPersonalizedPresenceFeatureImpressionPrior:]
- -[NTPBTodaySectionConfig setPresenceDeterminedByPersonalization:]
- OBJC_IVAR_$_NTPBAbsolutePersonalizedSectionPresenceConfig._cTRToHide
- OBJC_IVAR_$_NTPBAbsolutePersonalizedSectionPresenceConfig._cTRToShow
- OBJC_IVAR_$_NTPBAbsolutePersonalizedSectionPresenceConfig._has
- OBJC_IVAR_$_NTPBAbsolutePersonalizedSectionPresenceConfig._minProbabilityToShow
- OBJC_IVAR_$_NTPBAbsolutePersonalizedSectionPresenceConfig._sectionEdition
- OBJC_IVAR_$_NTPBPersonalizedSectionPresenceConfig._absoluteConfig
- OBJC_IVAR_$_NTPBPersonalizedSectionPresenceConfig._has
- OBJC_IVAR_$_NTPBPersonalizedSectionPresenceConfig._personalizationMethod
- OBJC_IVAR_$_NTPBPersonalizedSectionPresenceConfig._relativeConfig
- OBJC_IVAR_$_NTPBRelativePersonalizedSectionPresenceConfig._has
- OBJC_IVAR_$_NTPBRelativePersonalizedSectionPresenceConfig._scalar
- OBJC_IVAR_$_NTPBTodaySectionConfig._personalizedPresenceConfig
- OBJC_IVAR_$_NTPBTodaySectionConfig._personalizedPresenceFeatureClickPrior
- OBJC_IVAR_$_NTPBTodaySectionConfig._personalizedPresenceFeatureID
- OBJC_IVAR_$_NTPBTodaySectionConfig._personalizedPresenceFeatureImpressionPrior
- OBJC_IVAR_$_NTPBTodaySectionConfig._presenceDeterminedByPersonalization
- _NTPBAbsolutePersonalizedSectionPresenceConfigReadFrom
- _NTPBPersonalizedSectionPresenceConfigReadFrom
- _NTPBRelativePersonalizedSectionPresenceConfigReadFrom
- _OBJC_CLASS_$_NTPBAbsolutePersonalizedSectionPresenceConfig
- _OBJC_CLASS_$_NTPBPersonalizedSectionPresenceConfig
- _OBJC_CLASS_$_NTPBRelativePersonalizedSectionPresenceConfig
- _OBJC_METACLASS_$_NTPBAbsolutePersonalizedSectionPresenceConfig
- _OBJC_METACLASS_$_NTPBPersonalizedSectionPresenceConfig
- _OBJC_METACLASS_$_NTPBRelativePersonalizedSectionPresenceConfig
- __OBJC_$_INSTANCE_METHODS_NTPBAbsolutePersonalizedSectionPresenceConfig
- __OBJC_$_INSTANCE_METHODS_NTPBPersonalizedSectionPresenceConfig
- __OBJC_$_INSTANCE_METHODS_NTPBRelativePersonalizedSectionPresenceConfig
- __OBJC_$_INSTANCE_VARIABLES_NTPBAbsolutePersonalizedSectionPresenceConfig
- __OBJC_$_INSTANCE_VARIABLES_NTPBPersonalizedSectionPresenceConfig
- __OBJC_$_INSTANCE_VARIABLES_NTPBRelativePersonalizedSectionPresenceConfig
- __OBJC_$_PROP_LIST_NTPBAbsolutePersonalizedSectionPresenceConfig
- __OBJC_$_PROP_LIST_NTPBPersonalizedSectionPresenceConfig
- __OBJC_$_PROP_LIST_NTPBRelativePersonalizedSectionPresenceConfig
- __OBJC_CLASS_PROTOCOLS_$_NTPBAbsolutePersonalizedSectionPresenceConfig
- __OBJC_CLASS_PROTOCOLS_$_NTPBPersonalizedSectionPresenceConfig
- __OBJC_CLASS_PROTOCOLS_$_NTPBRelativePersonalizedSectionPresenceConfig
- __OBJC_CLASS_RO_$_NTPBAbsolutePersonalizedSectionPresenceConfig
- __OBJC_CLASS_RO_$_NTPBPersonalizedSectionPresenceConfig
- __OBJC_CLASS_RO_$_NTPBRelativePersonalizedSectionPresenceConfig
- __OBJC_METACLASS_RO_$_NTPBAbsolutePersonalizedSectionPresenceConfig
- __OBJC_METACLASS_RO_$_NTPBPersonalizedSectionPresenceConfig
- __OBJC_METACLASS_RO_$_NTPBRelativePersonalizedSectionPresenceConfig
- _fmod
- _fmodf
- _objc_msgSend$setAbsoluteConfig:
- _objc_msgSend$setPersonalizedPresenceConfig:
- _objc_msgSend$setPersonalizedPresenceFeatureID:
- _objc_msgSend$setRelativeConfig:
CStrings:
+ "$"
+ "%"
+ "@\"NTPBCKConfigurationFieldValue\""
+ "@\"NTPBCKDate\""
+ "@\"NTPBCKDateStatistics\""
+ "@\"NTPBCKIdentifier\""
+ "@\"NTPBCKLocale\""
+ "@\"NTPBCKOperation\""
+ "@\"NTPBCKQuery\""
+ "@\"NTPBCKQueryRetrieveRequest\""
+ "@\"NTPBCKQueryRetrieveResponse\""
+ "@\"NTPBCKRecord\""
+ "@\"NTPBCKRecordFieldIdentifier\""
+ "@\"NTPBCKRecordFieldValue\""
+ "@\"NTPBCKRecordIdentifier\""
+ "@\"NTPBCKRecordReference\""
+ "@\"NTPBCKRecordRetrieveRequest\""
+ "@\"NTPBCKRecordRetrieveResponse\""
+ "@\"NTPBCKRecordType\""
+ "@\"NTPBCKRecordZoneIdentifier\""
+ "@\"NTPBCKRequestOperationHeader\""
+ "@\"NTPBCKRequestedFields\""
+ "@\"NTPBCKResponseOperationResult\""
+ "@\"NTPBCKResponseOperationResultError\""
+ "@\"NTPBCKResponseOperationResultErrorClient\""
+ "@\"NTPBCKResponseOperationResultErrorExtension\""
+ "@\"NTPBCKResponseOperationResultErrorServer\""
+ "@\"NTPBPersonalizationParams\""
+ "@\"NTPBUserInfo\""
+ "NTPBCKConfiguration"
+ "NTPBCKConfigurationField"
+ "NTPBCKConfigurationFieldValue"
+ "NTPBCKDate"
+ "NTPBCKDateStatistics"
+ "NTPBCKIdentifier"
+ "NTPBCKLocale"
+ "NTPBCKOperation"
+ "NTPBCKQuery"
+ "NTPBCKQueryFilter"
+ "NTPBCKQueryRetrieveRequest"
+ "NTPBCKQueryRetrieveResponse"
+ "NTPBCKQueryRetrieveResponseQueryResult"
+ "NTPBCKQuerySort"
+ "NTPBCKRecord"
+ "NTPBCKRecordField"
+ "NTPBCKRecordFieldIdentifier"
+ "NTPBCKRecordFieldValue"
+ "NTPBCKRecordIdentifier"
+ "NTPBCKRecordReference"
+ "NTPBCKRecordRetrieveRequest"
+ "NTPBCKRecordRetrieveResponse"
+ "NTPBCKRecordType"
+ "NTPBCKRecordZoneIdentifier"
+ "NTPBCKRequestOperation"
+ "NTPBCKRequestOperationHeader"
+ "NTPBCKRequestedFields"
+ "NTPBCKResponseOperation"
+ "NTPBCKResponseOperationResult"
+ "NTPBCKResponseOperationResultError"
+ "NTPBCKResponseOperationResultErrorClient"
+ "NTPBCKResponseOperationResultErrorExtension"
+ "NTPBCKResponseOperationResultErrorServer"
+ "NTPBFetchRecordSpec"
+ "NTPBPersonalizationParams"
+ "NTPBRecipeListRecord"
+ "NTPBRecipeRecord"
+ "NTPBSmarterFetchRequest"
+ "NTPBSmarterFetchResponse"
+ "NTPBTagFollowed"
+ "NTPBTodayFeedPoolRequest"
+ "NTPBTodayFeedPoolResponse"
+ "NTPBUserInfo"
+ "T@\"NSData\",&,N,V_bytesValue"
+ "T@\"NSData\",&,N,V_clientChangeToken"
+ "T@\"NSData\",&,N,V_continuationMarker"
+ "T@\"NSData\",&,N,V_eventAggregationPersonalizationData"
+ "T@\"NSData\",&,N,V_extensionPayload"
+ "T@\"NSData\",&,N,V_personalizationData"
+ "T@\"NSData\",&,N,V_rapidUpdatePersonalizationData"
+ "T@\"NSData\",&,N,V_userInterestVector"
+ "T@\"NSMutableArray\",&,N,V_desiredFields"
+ "T@\"NSMutableArray\",&,N,V_enabledKeyboards"
+ "T@\"NSMutableArray\",&,N,V_fetchRecordSpecs"
+ "T@\"NSMutableArray\",&,N,V_fieldValues"
+ "T@\"NSMutableArray\",&,N,V_fields"
+ "T@\"NSMutableArray\",&,N,V_filters"
+ "T@\"NSMutableArray\",&,N,V_iAdSectionTagIDs"
+ "T@\"NSMutableArray\",&,N,V_linkedFields"
+ "T@\"NSMutableArray\",&,N,V_listValues"
+ "T@\"NSMutableArray\",&,N,V_preferredLanguages"
+ "T@\"NSMutableArray\",&,N,V_queryResults"
+ "T@\"NSMutableArray\",&,N,V_recipeIDs"
+ "T@\"NSMutableArray\",&,N,V_records"
+ "T@\"NSMutableArray\",&,N,V_smarterFetchSources"
+ "T@\"NSMutableArray\",&,N,V_sorts"
+ "T@\"NSMutableArray\",&,N,V_tagsFolloweds"
+ "T@\"NSMutableArray\",&,N,V_todayFeedPoolRequests"
+ "T@\"NSMutableArray\",&,N,V_todayFeedPoolResponses"
+ "T@\"NSMutableArray\",&,N,V_types"
+ "T@\"NSString\",&,N,V_activeKeyboard"
+ "T@\"NSString\",&,N,V_applicationBundle"
+ "T@\"NSString\",&,N,V_applicationContainer"
+ "T@\"NSString\",&,N,V_applicationVersion"
+ "T@\"NSString\",&,N,V_clientVersionETag"
+ "T@\"NSString\",&,N,V_contentType"
+ "T@\"NSString\",&,N,V_deviceAssignedName"
+ "T@\"NSString\",&,N,V_deviceFlowControlKey"
+ "T@\"NSString\",&,N,V_deviceHardwareID"
+ "T@\"NSString\",&,N,V_deviceHardwareVersion"
+ "T@\"NSString\",&,N,V_deviceLibraryName"
+ "T@\"NSString\",&,N,V_deviceLibraryVersion"
+ "T@\"NSString\",&,N,V_deviceSoftwareVersion"
+ "T@\"NSString\",&,N,V_errorDescription"
+ "T@\"NSString\",&,N,V_errorKey"
+ "T@\"NSString\",&,N,V_extensionName"
+ "T@\"NSString\",&,N,V_fetchSource"
+ "T@\"NSString\",&,N,V_fetchStrategy"
+ "T@\"NSString\",&,N,V_mmcsProtocolVersion"
+ "T@\"NSString\",&,N,V_operationGroupName"
+ "T@\"NSString\",&,N,V_operationUUID"
+ "T@\"NSString\",&,N,V_recipesRecirculationDataURL"
+ "T@\"NSString\",&,N,V_regionCode"
+ "T@\"NSString\",&,N,V_requestId"
+ "T@\"NSString\",&,N,V_smarterFetchStrategy"
+ "T@\"NSString\",&,N,V_storefrontId"
+ "T@\"NSString\",&,N,V_surfacedByChannelID"
+ "T@\"NSString\",&,N,V_surfacedBySectionID"
+ "T@\"NSString\",&,N,V_surfacedByTopicID"
+ "T@\"NSString\",&,N,V_thumbnailExtraLargeURL"
+ "T@\"NSString\",&,N,V_thumbnailLargeURL"
+ "T@\"NSString\",&,N,V_thumbnailSmallURL"
+ "T@\"NSString\",&,N,V_totalTime"
+ "T@\"NSString\",&,N,V_uivModelId"
+ "T@\"NSString\",&,N,V_userIDContainerID"
+ "T@\"NSString\",&,N,V_versionETag"
+ "T@\"NTPBCKConfigurationFieldValue\",&,N,V_value"
+ "T@\"NTPBCKDate\",&,N,V_creation"
+ "T@\"NTPBCKDate\",&,N,V_dateValue"
+ "T@\"NTPBCKDate\",&,N,V_modification"
+ "T@\"NTPBCKDateStatistics\",&,N,V_timeStatistics"
+ "T@\"NTPBCKIdentifier\",&,N,V_deviceIdentifier"
+ "T@\"NTPBCKIdentifier\",&,N,V_ownerIdentifier"
+ "T@\"NTPBCKIdentifier\",&,N,V_value"
+ "T@\"NTPBCKLocale\",&,N,V_locale"
+ "T@\"NTPBCKOperation\",&,N,V_request"
+ "T@\"NTPBCKOperation\",&,N,V_response"
+ "T@\"NTPBCKQuery\",&,N,V_query"
+ "T@\"NTPBCKQueryRetrieveRequest\",&,N,V_queryRetrieveRequest"
+ "T@\"NTPBCKQueryRetrieveResponse\",&,N,V_queryRetrieveResponse"
+ "T@\"NTPBCKRecord\",&,N,V_record"
+ "T@\"NTPBCKRecordFieldIdentifier\",&,N,V_fieldName"
+ "T@\"NTPBCKRecordFieldIdentifier\",&,N,V_identifier"
+ "T@\"NTPBCKRecordFieldValue\",&,N,V_fieldValue"
+ "T@\"NTPBCKRecordFieldValue\",&,N,V_value"
+ "T@\"NTPBCKRecordIdentifier\",&,N,V_identifier"
+ "T@\"NTPBCKRecordIdentifier\",&,N,V_recordIdentifier"
+ "T@\"NTPBCKRecordReference\",&,N,V_referenceValue"
+ "T@\"NTPBCKRecordRetrieveRequest\",&,N,V_recordRetrieveRequest"
+ "T@\"NTPBCKRecordRetrieveResponse\",&,N,V_recordRetrieveResponse"
+ "T@\"NTPBCKRecordType\",&,N,V_recordType"
+ "T@\"NTPBCKRecordType\",&,N,V_type"
+ "T@\"NTPBCKRecordZoneIdentifier\",&,N,V_zoneIdentifier"
+ "T@\"NTPBCKRequestOperationHeader\",&,N,V_header"
+ "T@\"NTPBCKRequestedFields\",&,N,V_requestedFields"
+ "T@\"NTPBCKResponseOperationResult\",&,N,V_result"
+ "T@\"NTPBCKResponseOperationResultError\",&,N,V_error"
+ "T@\"NTPBCKResponseOperationResultErrorClient\",&,N,V_clientError"
+ "T@\"NTPBCKResponseOperationResultErrorExtension\",&,N,V_extensionError"
+ "T@\"NTPBCKResponseOperationResultErrorServer\",&,N,V_serverError"
+ "T@\"NTPBDate\",&,N,V_lastReferenceDate"
+ "T@\"NTPBPersonalizationParams\",&,N,V_personalizationParams"
+ "T@\"NTPBUserInfo\",&,N,V_userInfo"
+ "TB,N,V_aLaCarteSubscribed"
+ "TB,N,V_boolValue"
+ "TB,N,V_deviceSoftwareIsAppleInternal"
+ "TB,N,V_distinct"
+ "TB,N,V_isEligibleForFoodGrouping"
+ "TB,N,V_isEligibleForFoodGroupingIfAutofavorited"
+ "TB,N,V_isEligibleForFoodGroupingIfFavorited"
+ "TB,N,V_last"
+ "TB,N,V_synchronousMode"
+ "TI,N,V_limit"
+ "TI,N,V_typeCode"
+ "TQ,N,V_applicationConfigVersion"
+ "TQ,N,V_created"
+ "TQ,N,V_deviceFlowControlBudget"
+ "TQ,N,V_deviceFlowControlBudgetCap"
+ "TQ,N,V_deviceProtocolVersion"
+ "TQ,N,V_expires"
+ "TQ,N,V_feedItemMaxCount"
+ "TQ,N,V_globalConfigVersion"
+ "TQ,N,V_operationGroupQuantity"
+ "Td,N,V_doubleValue"
+ "Td,N,V_time"
+ "Tf,N,V_deviceFlowControlRegeneration"
+ "Ti,N,V_applicationContainerEnvironment"
+ "Ti,N,V_code"
+ "Ti,N,V_isolationLevel"
+ "Ti,N,V_order"
+ "Ti,N,V_queryOperator"
+ "Ti,N,V_retryAfterSeconds"
+ "Ti,N,V_tagFollowMode"
+ "Ti,N,V_targetDatabase"
+ "Ti,N,V_ttlSecs"
+ "Tq,N,V_foodGroupingAvailability"
+ "Tq,N,V_fromTimestamp"
+ "Tq,N,V_longValue"
+ "Tq,N,V_nextFromTimestamp"
+ "Tq,N,V_previousFromTimestamp"
+ "Tq,N,V_signedValue"
+ "Tq,N,V_surfacedByFlags"
+ "Tq,N,V_thumbnailExtraLargeMetadata"
+ "Tq,N,V_thumbnailLargeMetadata"
+ "Tq,N,V_thumbnailSmallMetadata"
+ "_aLaCarteSubscribed"
+ "_activeKeyboard"
+ "_applicationBundle"
+ "_applicationConfigVersion"
+ "_applicationContainer"
+ "_applicationContainerEnvironment"
+ "_applicationVersion"
+ "_boolValue"
+ "_bytesValue"
+ "_clientChangeToken"
+ "_clientError"
+ "_clientVersionETag"
+ "_code"
+ "_continuationMarker"
+ "_created"
+ "_creation"
+ "_desiredFields"
+ "_deviceAssignedName"
+ "_deviceFlowControlBudget"
+ "_deviceFlowControlBudgetCap"
+ "_deviceFlowControlKey"
+ "_deviceFlowControlRegeneration"
+ "_deviceHardwareID"
+ "_deviceHardwareVersion"
+ "_deviceIdentifier"
+ "_deviceLibraryName"
+ "_deviceLibraryVersion"
+ "_deviceProtocolVersion"
+ "_deviceSoftwareIsAppleInternal"
+ "_deviceSoftwareVersion"
+ "_distinct"
+ "_doubleValue"
+ "_enabledKeyboards"
+ "_errorDescription"
+ "_errorKey"
+ "_eventAggregationPersonalizationData"
+ "_expires"
+ "_extensionError"
+ "_extensionName"
+ "_extensionPayload"
+ "_feedItemMaxCount"
+ "_fetchRecordSpecs"
+ "_fetchSource"
+ "_fetchStrategy"
+ "_fieldName"
+ "_fieldValue"
+ "_fieldValues"
+ "_fields"
+ "_filters"
+ "_foodGroupingAvailability"
+ "_fromTimestamp"
+ "_globalConfigVersion"
+ "_header"
+ "_iAdSectionTagIDs"
+ "_isEligibleForFoodGrouping"
+ "_isEligibleForFoodGroupingIfAutofavorited"
+ "_isEligibleForFoodGroupingIfFavorited"
+ "_isolationLevel"
+ "_last"
+ "_lastReferenceDate"
+ "_limit"
+ "_linkedFields"
+ "_listValues"
+ "_locale"
+ "_longValue"
+ "_mmcsProtocolVersion"
+ "_modification"
+ "_nextFromTimestamp"
+ "_operationGroupName"
+ "_operationGroupQuantity"
+ "_operationUUID"
+ "_ownerIdentifier"
+ "_personalizationData"
+ "_personalizationParams"
+ "_preferredLanguages"
+ "_previousFromTimestamp"
+ "_query"
+ "_queryOperator"
+ "_queryResults"
+ "_queryRetrieveRequest"
+ "_queryRetrieveResponse"
+ "_rapidUpdatePersonalizationData"
+ "_recipeIDs"
+ "_recipesRecirculationDataURL"
+ "_record"
+ "_recordIdentifier"
+ "_recordRetrieveRequest"
+ "_recordRetrieveResponse"
+ "_records"
+ "_referenceValue"
+ "_regionCode"
+ "_requestId"
+ "_requestedFields"
+ "_response"
+ "_result"
+ "_retryAfterSeconds"
+ "_serverError"
+ "_signedValue"
+ "_smarterFetchSources"
+ "_smarterFetchStrategy"
+ "_sorts"
+ "_storefrontId"
+ "_surfacedByChannelID"
+ "_surfacedByFlags"
+ "_surfacedBySectionID"
+ "_surfacedByTopicID"
+ "_synchronousMode"
+ "_tagFollowMode"
+ "_tagsFolloweds"
+ "_targetDatabase"
+ "_thumbnailExtraLargeMetadata"
+ "_thumbnailExtraLargeURL"
+ "_thumbnailLargeMetadata"
+ "_thumbnailLargeURL"
+ "_thumbnailSmallMetadata"
+ "_thumbnailSmallURL"
+ "_time"
+ "_timeStatistics"
+ "_todayFeedPoolRequests"
+ "_todayFeedPoolResponses"
+ "_totalTime"
+ "_ttlSecs"
+ "_typeCode"
+ "_types"
+ "_uivModelId"
+ "_userIDContainerID"
+ "_userInfo"
+ "_userInterestVector"
+ "_versionETag"
+ "_zoneIdentifier"
+ "aLaCarteSubscribed"
+ "a_la_carte_subscribed"
+ "activeKeyboard"
+ "addDesiredFields:"
+ "addEnabledKeyboards:"
+ "addFetchRecordSpecs:"
+ "addFieldValues:"
+ "addFields:"
+ "addFilters:"
+ "addIAdSectionTagIDs:"
+ "addLinkedFields:"
+ "addListValue:"
+ "addListValues:"
+ "addPreferredLanguages:"
+ "addQueryResults:"
+ "addRecipeIDs:"
+ "addRecords:"
+ "addSmarterFetchSources:"
+ "addSorts:"
+ "addTagsFollowed:"
+ "addTodayFeedPoolRequests:"
+ "addTodayFeedPoolResponse:"
+ "addTypes:"
+ "applicationBundle"
+ "applicationConfigVersion"
+ "applicationContainer"
+ "applicationContainerEnvironment"
+ "applicationVersion"
+ "boolValue"
+ "bytesValue"
+ "clearDesiredFields"
+ "clearEnabledKeyboards"
+ "clearFetchRecordSpecs"
+ "clearFieldValues"
+ "clearFields"
+ "clearFilters"
+ "clearIAdSectionTagIDs"
+ "clearLinkedFields"
+ "clearListValues"
+ "clearPreferredLanguages"
+ "clearQueryResults"
+ "clearRecipeIDs"
+ "clearRecords"
+ "clearSmarterFetchSources"
+ "clearSorts"
+ "clearTagsFolloweds"
+ "clearTodayFeedPoolRequests"
+ "clearTodayFeedPoolResponses"
+ "clearTypes"
+ "clientChangeToken"
+ "clientError"
+ "clientVersionETag"
+ "code"
+ "continuationMarker"
+ "created"
+ "creation"
+ "desiredFields"
+ "desiredFieldsAtIndex:"
+ "desiredFieldsCount"
+ "desiredFieldsType"
+ "desired_fields"
+ "deviceAssignedName"
+ "deviceFlowControlBudget"
+ "deviceFlowControlBudgetCap"
+ "deviceFlowControlKey"
+ "deviceFlowControlRegeneration"
+ "deviceHardwareID"
+ "deviceHardwareVersion"
+ "deviceIdentifier"
+ "deviceLibraryName"
+ "deviceLibraryVersion"
+ "deviceProtocolVersion"
+ "deviceSoftwareIsAppleInternal"
+ "deviceSoftwareVersion"
+ "distinct"
+ "doubleValue"
+ "enabledKeyboards"
+ "enabledKeyboardsAtIndex:"
+ "enabledKeyboardsCount"
+ "enabledKeyboardsType"
+ "errorDescription"
+ "errorKey"
+ "eventAggregationPersonalizationData"
+ "event_aggregation_personalization_data"
+ "expires"
+ "extensionError"
+ "extensionName"
+ "extensionPayload"
+ "feedItemMaxCount"
+ "feed_item_max_count"
+ "fetchRecordSpecs"
+ "fetchRecordSpecsAtIndex:"
+ "fetchRecordSpecsCount"
+ "fetchRecordSpecsType"
+ "fetchSource"
+ "fetchStrategy"
+ "fetch_record_specs"
+ "fetch_source"
+ "fetch_strategy"
+ "fieldName"
+ "fieldValue"
+ "fieldValues"
+ "fieldValuesAtIndex:"
+ "fieldValuesCount"
+ "fieldValuesType"
+ "fields"
+ "fieldsAtIndex:"
+ "fieldsCount"
+ "fieldsType"
+ "filters"
+ "filtersAtIndex:"
+ "filtersCount"
+ "filtersType"
+ "foodGroupingAvailability"
+ "food_grouping_availability"
+ "fromTimestamp"
+ "from_timestamp"
+ "globalConfigVersion"
+ "hasALaCarteSubscribed"
+ "hasActiveKeyboard"
+ "hasApplicationBundle"
+ "hasApplicationConfigVersion"
+ "hasApplicationContainer"
+ "hasApplicationContainerEnvironment"
+ "hasApplicationVersion"
+ "hasBoolValue"
+ "hasBytesValue"
+ "hasClientChangeToken"
+ "hasClientError"
+ "hasClientVersionETag"
+ "hasCode"
+ "hasContinuationMarker"
+ "hasCreated"
+ "hasCreation"
+ "hasDeviceAssignedName"
+ "hasDeviceFlowControlBudget"
+ "hasDeviceFlowControlBudgetCap"
+ "hasDeviceFlowControlKey"
+ "hasDeviceFlowControlRegeneration"
+ "hasDeviceHardwareID"
+ "hasDeviceHardwareVersion"
+ "hasDeviceIdentifier"
+ "hasDeviceLibraryName"
+ "hasDeviceLibraryVersion"
+ "hasDeviceProtocolVersion"
+ "hasDeviceSoftwareIsAppleInternal"
+ "hasDeviceSoftwareVersion"
+ "hasDistinct"
+ "hasDoubleValue"
+ "hasErrorDescription"
+ "hasErrorKey"
+ "hasEventAggregationPersonalizationData"
+ "hasExpires"
+ "hasExtensionError"
+ "hasExtensionName"
+ "hasExtensionPayload"
+ "hasFeedItemMaxCount"
+ "hasFetchSource"
+ "hasFetchStrategy"
+ "hasFieldName"
+ "hasFieldValue"
+ "hasFoodGroupingAvailability"
+ "hasFromTimestamp"
+ "hasGlobalConfigVersion"
+ "hasHeader"
+ "hasIsEligibleForFoodGrouping"
+ "hasIsEligibleForFoodGroupingIfAutofavorited"
+ "hasIsEligibleForFoodGroupingIfFavorited"
+ "hasIsolationLevel"
+ "hasLast"
+ "hasLastReferenceDate"
+ "hasLimit"
+ "hasLocale"
+ "hasLongValue"
+ "hasMmcsProtocolVersion"
+ "hasModification"
+ "hasNextFromTimestamp"
+ "hasOperationGroupName"
+ "hasOperationGroupQuantity"
+ "hasOperationUUID"
+ "hasOwnerIdentifier"
+ "hasPersonalizationData"
+ "hasPersonalizationParams"
+ "hasPreviousFromTimestamp"
+ "hasQuery"
+ "hasQueryOperator"
+ "hasQueryRetrieveRequest"
+ "hasQueryRetrieveResponse"
+ "hasRapidUpdatePersonalizationData"
+ "hasRecipesRecirculationDataURL"
+ "hasRecord"
+ "hasRecordIdentifier"
+ "hasRecordRetrieveRequest"
+ "hasRecordRetrieveResponse"
+ "hasReferenceValue"
+ "hasRegionCode"
+ "hasRequestId"
+ "hasRequestedFields"
+ "hasResponse"
+ "hasResult"
+ "hasRetryAfterSeconds"
+ "hasServerError"
+ "hasSignedValue"
+ "hasSmarterFetchStrategy"
+ "hasStorefrontId"
+ "hasSurfacedByChannelID"
+ "hasSurfacedByFlags"
+ "hasSurfacedBySectionID"
+ "hasSurfacedByTopicID"
+ "hasSynchronousMode"
+ "hasTagFollowMode"
+ "hasTargetDatabase"
+ "hasThumbnailExtraLargeMetadata"
+ "hasThumbnailExtraLargeURL"
+ "hasThumbnailLargeMetadata"
+ "hasThumbnailLargeURL"
+ "hasThumbnailSmallMetadata"
+ "hasThumbnailSmallURL"
+ "hasTime"
+ "hasTimeStatistics"
+ "hasTotalTime"
+ "hasTtlSecs"
+ "hasTypeCode"
+ "hasUivModelId"
+ "hasUserIDContainerID"
+ "hasUserInfo"
+ "hasUserInterestVector"
+ "hasVersionETag"
+ "hasZoneIdentifier"
+ "header"
+ "iAdSectionTagIDs"
+ "iAdSectionTagIDsAtIndex:"
+ "iAdSectionTagIDsCount"
+ "iAdSectionTagIDsType"
+ "i_ad_section_tag_IDs"
+ "isEligibleForFoodGrouping"
+ "isEligibleForFoodGroupingIfAutofavorited"
+ "isEligibleForFoodGroupingIfFavorited"
+ "is_eligible_for_food_grouping"
+ "is_eligible_for_food_grouping_if_autofavorited"
+ "is_eligible_for_food_grouping_if_favorited"
+ "isolationLevel"
+ "last"
+ "lastReferenceDate"
+ "last_reference_date"
+ "limit"
+ "linkedFields"
+ "linkedFieldsAtIndex:"
+ "linkedFieldsCount"
+ "linkedFieldsType"
+ "linked_fields"
+ "listValue"
+ "listValueAtIndex:"
+ "listValueType"
+ "listValues"
+ "listValuesAtIndex:"
+ "listValuesCount"
+ "listValuesType"
+ "locale"
+ "longValue"
+ "mmcsProtocolVersion"
+ "modification"
+ "nextFromTimestamp"
+ "next_from_timestamp"
+ "operationGroupName"
+ "operationGroupQuantity"
+ "operationUUID"
+ "ownerIdentifier"
+ "personalizationData"
+ "personalizationParams"
+ "personalization_data"
+ "personalization_params"
+ "preferredLanguages"
+ "preferredLanguagesAtIndex:"
+ "preferredLanguagesCount"
+ "preferredLanguagesType"
+ "preferred_languages"
+ "previousFromTimestamp"
+ "previous_from_timestamp"
+ "query"
+ "queryOperator"
+ "queryResults"
+ "queryResultsAtIndex:"
+ "queryResultsCount"
+ "queryResultsType"
+ "queryRetrieveRequest"
+ "queryRetrieveResponse"
+ "rapidUpdatePersonalizationData"
+ "rapid_update_personalization_data"
+ "recipeIDs"
+ "recipeIDsAtIndex:"
+ "recipeIDsCount"
+ "recipeIDsType"
+ "recipe_IDs"
+ "recipesRecirculationDataURL"
+ "recipes_recirculation_data_URL"
+ "record"
+ "recordIdentifier"
+ "recordRetrieveRequest"
+ "recordRetrieveResponse"
+ "records"
+ "recordsAtIndex:"
+ "recordsCount"
+ "recordsType"
+ "referenceValue"
+ "regionCode"
+ "requestId"
+ "request_id"
+ "requestedFields"
+ "response"
+ "result"
+ "retryAfterSeconds"
+ "serverError"
+ "setALaCarteSubscribed:"
+ "setActiveKeyboard:"
+ "setApplicationBundle:"
+ "setApplicationConfigVersion:"
+ "setApplicationContainer:"
+ "setApplicationContainerEnvironment:"
+ "setApplicationVersion:"
+ "setBoolValue:"
+ "setBytesValue:"
+ "setClientChangeToken:"
+ "setClientError:"
+ "setClientVersionETag:"
+ "setCode:"
+ "setContinuationMarker:"
+ "setCreated:"
+ "setCreation:"
+ "setDesiredFields:"
+ "setDeviceAssignedName:"
+ "setDeviceFlowControlBudget:"
+ "setDeviceFlowControlBudgetCap:"
+ "setDeviceFlowControlKey:"
+ "setDeviceFlowControlRegeneration:"
+ "setDeviceHardwareID:"
+ "setDeviceHardwareVersion:"
+ "setDeviceIdentifier:"
+ "setDeviceLibraryName:"
+ "setDeviceLibraryVersion:"
+ "setDeviceProtocolVersion:"
+ "setDeviceSoftwareIsAppleInternal:"
+ "setDeviceSoftwareVersion:"
+ "setDistinct:"
+ "setDoubleValue:"
+ "setEnabledKeyboards:"
+ "setErrorDescription:"
+ "setErrorKey:"
+ "setEventAggregationPersonalizationData:"
+ "setExpires:"
+ "setExtensionError:"
+ "setExtensionName:"
+ "setExtensionPayload:"
+ "setFeedItemMaxCount:"
+ "setFetchRecordSpecs:"
+ "setFetchSource:"
+ "setFetchStrategy:"
+ "setFieldName:"
+ "setFieldValue:"
+ "setFieldValues:"
+ "setFields:"
+ "setFilters:"
+ "setFoodGroupingAvailability:"
+ "setFromTimestamp:"
+ "setGlobalConfigVersion:"
+ "setHasALaCarteSubscribed:"
+ "setHasApplicationConfigVersion:"
+ "setHasApplicationContainerEnvironment:"
+ "setHasBoolValue:"
+ "setHasCode:"
+ "setHasCreated:"
+ "setHasDeviceFlowControlBudget:"
+ "setHasDeviceFlowControlBudgetCap:"
+ "setHasDeviceFlowControlRegeneration:"
+ "setHasDeviceProtocolVersion:"
+ "setHasDeviceSoftwareIsAppleInternal:"
+ "setHasDistinct:"
+ "setHasDoubleValue:"
+ "setHasExpires:"
+ "setHasFeedItemMaxCount:"
+ "setHasFoodGroupingAvailability:"
+ "setHasFromTimestamp:"
+ "setHasGlobalConfigVersion:"
+ "setHasIsEligibleForFoodGrouping:"
+ "setHasIsEligibleForFoodGroupingIfAutofavorited:"
+ "setHasIsEligibleForFoodGroupingIfFavorited:"
+ "setHasIsolationLevel:"
+ "setHasLast:"
+ "setHasLimit:"
+ "setHasLongValue:"
+ "setHasNextFromTimestamp:"
+ "setHasOperationGroupQuantity:"
+ "setHasPreviousFromTimestamp:"
+ "setHasQueryOperator:"
+ "setHasRetryAfterSeconds:"
+ "setHasSignedValue:"
+ "setHasSurfacedByFlags:"
+ "setHasSynchronousMode:"
+ "setHasTagFollowMode:"
+ "setHasTargetDatabase:"
+ "setHasThumbnailExtraLargeMetadata:"
+ "setHasThumbnailLargeMetadata:"
+ "setHasThumbnailSmallMetadata:"
+ "setHasTime:"
+ "setHasTtlSecs:"
+ "setHasTypeCode:"
+ "setHeader:"
+ "setIAdSectionTagIDs:"
+ "setIsEligibleForFoodGrouping:"
+ "setIsEligibleForFoodGroupingIfAutofavorited:"
+ "setIsEligibleForFoodGroupingIfFavorited:"
+ "setIsolationLevel:"
+ "setLast:"
+ "setLastReferenceDate:"
+ "setLimit:"
+ "setLinkedFields:"
+ "setListValues:"
+ "setLocale:"
+ "setLongValue:"
+ "setMmcsProtocolVersion:"
+ "setModification:"
+ "setNextFromTimestamp:"
+ "setOperationGroupName:"
+ "setOperationGroupQuantity:"
+ "setOperationUUID:"
+ "setOwnerIdentifier:"
+ "setPersonalizationData:"
+ "setPersonalizationParams:"
+ "setPreferredLanguages:"
+ "setPreviousFromTimestamp:"
+ "setQuery:"
+ "setQueryOperator:"
+ "setQueryResults:"
+ "setQueryRetrieveRequest:"
+ "setQueryRetrieveResponse:"
+ "setRapidUpdatePersonalizationData:"
+ "setRecipeIDs:"
+ "setRecipesRecirculationDataURL:"
+ "setRecord:"
+ "setRecordIdentifier:"
+ "setRecordRetrieveRequest:"
+ "setRecordRetrieveResponse:"
+ "setRecords:"
+ "setReferenceValue:"
+ "setRegionCode:"
+ "setRequestId:"
+ "setRequestedFields:"
+ "setResponse:"
+ "setResult:"
+ "setRetryAfterSeconds:"
+ "setServerError:"
+ "setSignedValue:"
+ "setSmarterFetchSources:"
+ "setSmarterFetchStrategy:"
+ "setSorts:"
+ "setStorefrontId:"
+ "setSurfacedByChannelID:"
+ "setSurfacedByFlags:"
+ "setSurfacedBySectionID:"
+ "setSurfacedByTopicID:"
+ "setSynchronousMode:"
+ "setTagFollowMode:"
+ "setTagsFolloweds:"
+ "setTargetDatabase:"
+ "setThumbnailExtraLargeMetadata:"
+ "setThumbnailExtraLargeURL:"
+ "setThumbnailLargeMetadata:"
+ "setThumbnailLargeURL:"
+ "setThumbnailSmallMetadata:"
+ "setThumbnailSmallURL:"
+ "setTime:"
+ "setTimeStatistics:"
+ "setTodayFeedPoolRequests:"
+ "setTodayFeedPoolResponses:"
+ "setTotalTime:"
+ "setTtlSecs:"
+ "setTypeCode:"
+ "setTypes:"
+ "setUivModelId:"
+ "setUserIDContainerID:"
+ "setUserInfo:"
+ "setUserInterestVector:"
+ "setVersionETag:"
+ "setZoneIdentifier:"
+ "signedValue"
+ "smarterFetchSources"
+ "smarterFetchSourcesAtIndex:"
+ "smarterFetchSourcesCount"
+ "smarterFetchSourcesType"
+ "smarterFetchStrategy"
+ "smarter_fetch_sources"
+ "smarter_fetch_strategy"
+ "sorts"
+ "sortsAtIndex:"
+ "sortsCount"
+ "sortsType"
+ "storefrontId"
+ "storefront_id"
+ "surfacedByChannelID"
+ "surfacedByFlags"
+ "surfacedBySectionID"
+ "surfacedByTopicID"
+ "surfaced_by_channel_ID"
+ "surfaced_by_flags"
+ "surfaced_by_section_ID"
+ "surfaced_by_topic_ID"
+ "synchronousMode"
+ "tagFollowMode"
+ "tag_follow_mode"
+ "tagsFollowedAtIndex:"
+ "tagsFollowedType"
+ "tagsFolloweds"
+ "tagsFollowedsCount"
+ "tags_followed"
+ "targetDatabase"
+ "thumbnailExtraLargeMetadata"
+ "thumbnailExtraLargeURL"
+ "thumbnailLargeMetadata"
+ "thumbnailLargeURL"
+ "thumbnailSmallMetadata"
+ "thumbnailSmallURL"
+ "thumbnail_extra_large_URL"
+ "thumbnail_extra_large_metadata"
+ "thumbnail_large_URL"
+ "thumbnail_large_metadata"
+ "thumbnail_small_URL"
+ "thumbnail_small_metadata"
+ "time"
+ "timeStatistics"
+ "todayFeedPoolRequests"
+ "todayFeedPoolRequestsAtIndex:"
+ "todayFeedPoolRequestsCount"
+ "todayFeedPoolRequestsType"
+ "todayFeedPoolResponseAtIndex:"
+ "todayFeedPoolResponseType"
+ "todayFeedPoolResponses"
+ "todayFeedPoolResponsesCount"
+ "today_feed_pool_requests"
+ "today_feed_pool_response"
+ "totalTime"
+ "total_time"
+ "ttlSecs"
+ "ttl_secs"
+ "typeCode"
+ "types"
+ "typesAtIndex:"
+ "typesCount"
+ "typesType"
+ "uivModelId"
+ "uiv_model_id"
+ "userIDContainerID"
+ "userInfo"
+ "userInterestVector"
+ "user_info"
+ "user_interest_vector"
+ "versionETag"
+ "zoneIdentifier"
+ "{?=\"applicationConfigVersion\"b1\"deviceFlowControlBudget\"b1\"deviceFlowControlBudgetCap\"b1\"deviceProtocolVersion\"b1\"globalConfigVersion\"b1\"operationGroupQuantity\"b1\"applicationContainerEnvironment\"b1\"deviceFlowControlRegeneration\"b1\"isolationLevel\"b1\"targetDatabase\"b1\"deviceSoftwareIsAppleInternal\"b1}"
+ "{?=\"behaviorFlags\"b1\"contentProvider\"b1\"foodGroupingAvailability\"b1\"minimumNewsVersion\"b1\"nameImageBaselineShift\"b1\"nameImageScaleFactor\"b1\"propertyFlags\"b1\"propertyFlagsLocalized\"b1\"score\"b1\"subscriptionRate\"b1\"groupingAvailability\"b1\"type\"b1\"hideAccessoryText\"b1\"isDeprecated\"b1\"isExplicitContent\"b1\"isHidden\"b1\"isNotificationEnabled\"b1\"isPublic\"b1\"isSportsRecommendable\"b1\"publisherPaidLeakyPaywallOptOut\"b1\"publisherPaidWebOptIn\"b1}"
+ "{?=\"bodyTextLength\"b1\"conditionalScore\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"surfacedByFlags\"b1\"storyType\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isAIGenerated\"b1\"isBundlePaid\"b1\"isCoread\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
+ "{?=\"cachedResultCutoffTime\"b1\"fallbackOrder\"b1\"interSectionFilteringOptions\"b1\"intraSectionFilteringOptions\"b1\"maximumStoriesAllocation\"b1\"minimumStoriesAllocation\"b1\"paywalledStoriesMaxCount\"b1\"seenArticlesMinimumTimeSinceFirstSeenToFilter\"b1\"promotionCriterion\"b1\"readArticlesFilterMethod\"b1\"sectionType\"b1\"seenArticlesFilterMethod\"b1\"filterNonSubscribedInFavoritesOnlyMode\"b1\"glanceable\"b1\"shownInFavoritesOnlyMode\"b1}"
+ "{?=\"code\"b1}"
+ "{?=\"created\"b1\"expires\"b1}"
+ "{?=\"cutoffTime\"b1\"feedItemMaxCount\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"fetchingBin\"b1}"
+ "{?=\"doubleValue\"b1\"longValue\"b1\"type\"b1\"boolValue\"b1}"
+ "{?=\"doubleValue\"b1\"signedValue\"b1\"type\"b1}"
+ "{?=\"flowRate\"b1\"ontologyLevel\"b1\"quality\"b1\"subscriptionRate\"b1\"hardFollowRequiredForGrouping\"b1\"isDisallowedFromGrouping\"b1\"isEligibleForFoodGrouping\"b1\"isEligibleForFoodGroupingIfAutofavorited\"b1\"isEligibleForFoodGroupingIfFavorited\"b1\"isEligibleForGrouping\"b1\"isEligibleForGroupingIfAutofavorited\"b1\"isEligibleForGroupingIfFavorited\"b1\"isHidden\"b1\"isManagedTopic\"b1\"isManagedTopicWinner\"b1}"
+ "{?=\"fromTimestamp\"b1\"previousFromTimestamp\"b1}"
+ "{?=\"limit\"b1}"
+ "{?=\"minimumNewsVersion\"b1\"thumbnailExtraLargeMetadata\"b1\"thumbnailFocalFrame\"b1\"thumbnailLargeMetadata\"b1\"thumbnailMediumMetadata\"b1\"thumbnailSmallMetadata\"b1\"isDraft\"b1\"isPaid\"b1}"
+ "{?=\"nextFromTimestamp\"b1\"ttlSecs\"b1}"
+ "{?=\"order\"b1}"
+ "{?=\"queryOperator\"b1\"distinct\"b1}"
+ "{?=\"retryAfterSeconds\"b1}"
+ "{?=\"subscriberType\"b1}"
+ "{?=\"tagFollowMode\"b1\"aLaCarteSubscribed\"b1}"
+ "{?=\"time\"b1}"
+ "{?=\"type\"b1\"last\"b1\"synchronousMode\"b1}"
+ "{?=\"typeCode\"b1}"
- "@\"NTPBAbsolutePersonalizedSectionPresenceConfig\""
- "@\"NTPBPersonalizedSectionPresenceConfig\""
- "@\"NTPBRelativePersonalizedSectionPresenceConfig\""
- "CTR_to_hide"
- "CTR_to_show"
- "NTPBAbsolutePersonalizedSectionPresenceConfig"
- "NTPBPersonalizedSectionPresenceConfig"
- "NTPBRelativePersonalizedSectionPresenceConfig"
- "T@\"NSString\",&,N,V_personalizedPresenceFeatureID"
- "T@\"NTPBAbsolutePersonalizedSectionPresenceConfig\",&,N,V_absoluteConfig"
- "T@\"NTPBPersonalizedSectionPresenceConfig\",&,N,V_personalizedPresenceConfig"
- "T@\"NTPBRelativePersonalizedSectionPresenceConfig\",&,N,V_relativeConfig"
- "TB,N,V_presenceDeterminedByPersonalization"
- "TQ,N,V_personalizedPresenceFeatureClickPrior"
- "TQ,N,V_personalizedPresenceFeatureImpressionPrior"
- "TQ,N,V_sectionEdition"
- "Td,N,V_cTRToHide"
- "Td,N,V_cTRToShow"
- "Td,N,V_minProbabilityToShow"
- "Td,N,V_scalar"
- "Ti,N,V_personalizationMethod"
- "_absoluteConfig"
- "_cTRToHide"
- "_cTRToShow"
- "_minProbabilityToShow"
- "_personalizationMethod"
- "_personalizedPresenceConfig"
- "_personalizedPresenceFeatureClickPrior"
- "_personalizedPresenceFeatureID"
- "_personalizedPresenceFeatureImpressionPrior"
- "_presenceDeterminedByPersonalization"
- "_relativeConfig"
- "_scalar"
- "_sectionEdition"
- "absoluteConfig"
- "absolute_config"
- "cTRToHide"
- "cTRToShow"
- "hasAbsoluteConfig"
- "hasCTRToHide"
- "hasCTRToShow"
- "hasMinProbabilityToShow"
- "hasPersonalizationMethod"
- "hasPersonalizedPresenceConfig"
- "hasPersonalizedPresenceFeatureClickPrior"
- "hasPersonalizedPresenceFeatureID"
- "hasPersonalizedPresenceFeatureImpressionPrior"
- "hasPresenceDeterminedByPersonalization"
- "hasRelativeConfig"
- "hasScalar"
- "hasSectionEdition"
- "minProbabilityToShow"
- "min_probability_to_show"
- "personalizationMethod"
- "personalization_method"
- "personalizedPresenceConfig"
- "personalizedPresenceFeatureClickPrior"
- "personalizedPresenceFeatureID"
- "personalizedPresenceFeatureImpressionPrior"
- "personalized_presence_config"
- "personalized_presence_feature_ID"
- "personalized_presence_feature_click_prior"
- "personalized_presence_feature_impression_prior"
- "presenceDeterminedByPersonalization"
- "presence_determined_by_personalization"
- "relativeConfig"
- "relative_config"
- "scalar"
- "sectionEdition"
- "section_edition"
- "setAbsoluteConfig:"
- "setCTRToHide:"
- "setCTRToShow:"
- "setHasCTRToHide:"
- "setHasCTRToShow:"
- "setHasMinProbabilityToShow:"
- "setHasPersonalizationMethod:"
- "setHasPersonalizedPresenceFeatureClickPrior:"
- "setHasPersonalizedPresenceFeatureImpressionPrior:"
- "setHasPresenceDeterminedByPersonalization:"
- "setHasScalar:"
- "setHasSectionEdition:"
- "setMinProbabilityToShow:"
- "setPersonalizationMethod:"
- "setPersonalizedPresenceConfig:"
- "setPersonalizedPresenceFeatureClickPrior:"
- "setPersonalizedPresenceFeatureID:"
- "setPersonalizedPresenceFeatureImpressionPrior:"
- "setPresenceDeterminedByPersonalization:"
- "setRelativeConfig:"
- "setScalar:"
- "setSectionEdition:"
- "{?=\"behaviorFlags\"b1\"contentProvider\"b1\"minimumNewsVersion\"b1\"nameImageBaselineShift\"b1\"nameImageScaleFactor\"b1\"propertyFlags\"b1\"propertyFlagsLocalized\"b1\"score\"b1\"subscriptionRate\"b1\"groupingAvailability\"b1\"type\"b1\"hideAccessoryText\"b1\"isDeprecated\"b1\"isExplicitContent\"b1\"isHidden\"b1\"isNotificationEnabled\"b1\"isPublic\"b1\"isSportsRecommendable\"b1\"publisherPaidLeakyPaywallOptOut\"b1\"publisherPaidWebOptIn\"b1}"
- "{?=\"bodyTextLength\"b1\"conditionalScore\"b1\"contentType\"b1\"feedHalfLifeMilliseconds\"b1\"globalUserFeedback\"b1\"minimumNewsVersion\"b1\"order\"b1\"publishDateMilliseconds\"b1\"publisherArticleVersion\"b1\"hasAudioTrack\"b1\"hasThumbnail\"b1\"hasVideo\"b1\"hasVideoStillImage\"b1\"isAIGenerated\"b1\"isBundlePaid\"b1\"isCoread\"b1\"isEvergreen\"b1\"isExplicitContent\"b1\"isFeatureCandidate\"b1\"isFeatured\"b1\"isFromBlockedStorefront\"b1\"isHiddenFromAutoFavorites\"b1\"isIssueOnly\"b1\"isPaid\"b1\"isSponsored\"b1\"reduceVisibility\"b1\"reduceVisibilityForNonFollowers\"b1\"webConverted\"b1}"
- "{?=\"cTRToHide\"b1\"cTRToShow\"b1\"minProbabilityToShow\"b1\"sectionEdition\"b1}"
- "{?=\"cachedResultCutoffTime\"b1\"fallbackOrder\"b1\"interSectionFilteringOptions\"b1\"intraSectionFilteringOptions\"b1\"maximumStoriesAllocation\"b1\"minimumStoriesAllocation\"b1\"paywalledStoriesMaxCount\"b1\"personalizedPresenceFeatureClickPrior\"b1\"personalizedPresenceFeatureImpressionPrior\"b1\"seenArticlesMinimumTimeSinceFirstSeenToFilter\"b1\"promotionCriterion\"b1\"readArticlesFilterMethod\"b1\"sectionType\"b1\"seenArticlesFilterMethod\"b1\"filterNonSubscribedInFavoritesOnlyMode\"b1\"glanceable\"b1\"presenceDeterminedByPersonalization\"b1\"shownInFavoritesOnlyMode\"b1}"
- "{?=\"cutoffTime\"b1\"feedMaxCount\"b1\"headlinesPerFeedFetchCount\"b1\"localNewsPromotionIndex\"b1\"minimumUpdateInterval\"b1\"subscriptionsFetchCount\"b1\"fetchingBin\"b1}"
- "{?=\"flowRate\"b1\"ontologyLevel\"b1\"quality\"b1\"subscriptionRate\"b1\"hardFollowRequiredForGrouping\"b1\"isDisallowedFromGrouping\"b1\"isEligibleForGrouping\"b1\"isEligibleForGroupingIfAutofavorited\"b1\"isEligibleForGroupingIfFavorited\"b1\"isHidden\"b1\"isManagedTopic\"b1\"isManagedTopicWinner\"b1}"
- "{?=\"personalizationMethod\"b1}"
- "{?=\"scalar\"b1}"

```
