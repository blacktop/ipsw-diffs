## ShazamInsights

> `/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights`

```diff

-322.5.1.0.0
-  __TEXT.__text: 0xafb8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0xd00
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xb66
-  __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__oslogstring: 0x353
-  __TEXT.__unwind_info: 0x358
-  __TEXT.__objc_classname: 0x2e1
-  __TEXT.__objc_methname: 0x25b5
-  __TEXT.__objc_methtype: 0x729
-  __TEXT.__objc_stubs: 0x2020
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x578
-  __DATA_CONST.__objc_classlist: 0xe8
+423.0.29.0.0
+  __TEXT.__text: 0x39ec
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_methlist: 0x5d0
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x386
+  __TEXT.__oslogstring: 0xb5
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_classname: 0x159
+  __TEXT.__objc_methname: 0x10cd
+  __TEXT.__objc_methtype: 0x3a2
+  __TEXT.__objc_stubs: 0xb80
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x978
-  __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x288
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x2000
+  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0xd0
-  __DATA.__data: 0x1e8
-  __DATA.__bss: 0x28
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x54
+  __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ShazamKit.framework/ShazamKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C85A3815-2CC1-33CC-9E42-EF496DE2E5D9
-  Functions: 270
-  Symbols:   1263
-  CStrings:  720
+  UUID: 42BC674E-43AB-303C-8C84-8EDE0295B152
+  Functions: 107
+  Symbols:   541
+  CStrings:  328
 
Symbols:
- +[SHClusterController artistClusterDefaultLocationURL]
- +[SHClusterController databaseURLForName:]
- +[SHClusterController trackClusterDefaultLocationURL]
- +[SHClusterImporterUtils buildTemporaryClusterURLWithError:]
- +[SHClusterImporterUtils cachesDirectory]
- +[SHClusterImporterUtils clearTemporaryDatabaseFileAtURL:withError:]
- +[SHClusterImporterUtils copyDatabaseFromURL:toDatabaseDestinationURL:error:]
- +[SHClusterImporterUtils importerForFile:]
- +[SHClusterLoader loadDataForRequest:storefront:configuration:completionHandler:]
- +[SHClusterMetadataQuery dataStoreTypeFromString:]
- +[SHClusterMetadataQuery dateFormatter]
- +[SHClusterMetadataQuery metadataFromDatabaseAtLocation:error:]
- +[SHClusterMetadataQuery stringFromStoreType:]
- +[SHClusterMetadataQuery writeMetadata:toDatabaseAtLocation:error:]
- +[SHClusterQuery artistsCluster]
- +[SHClusterQuery artistsCluster].cold.1
- +[SHClusterQuery clusterForType:]
- +[SHClusterQuery tracksCluster]
- +[SHClusterQuery tracksCluster].cold.1
- +[SHClusterSQLiteDataStore sqliteDatabaseExistsAtURL:]
- +[SHClusterStatementRunner supportedKeys]
- +[SHFileChecksum checksumDataForFile:withError:]
- +[SHFileChecksum checksumForFile:withError:]
- +[SHMediaItemPropertyCollection collectionWithArray:representingProperty:]
- +[SHSQLiteUtils closeDatabase:error:]
- +[SHSQLiteUtils commitTransactionOnDatabase:]
- +[SHSQLiteUtils createDatabase:atURL:error:]
- +[SHSQLiteUtils database:hasPopulatedTable:error:]
- +[SHSQLiteUtils defenseAgainstBadDatabase:]
- +[SHSQLiteUtils openDatabase:atURL:error:]
- +[SHSQLiteUtils queryStringForCount:]
- +[SHSQLiteUtils runNoResultSQL:onDatabase:error:]
- +[SHSQLiteUtils runSQL:onDatabase:replacingTokens:withObjects:rowHandler:error:]
- +[SHSQLiteUtils startTransactionOnDatabase:]
- -[SHCDNDataFetcher doesRequestEtag:matchInResponse:]
- -[SHCDNDataFetcher fetchClusterURL:forCurrentStorefront:cachedUniqueHash:completionHandler:]
- -[SHClusterController .cxx_destruct]
- -[SHClusterController affinityGroupsAtCohesionLevel:forQuery:queryCollection:filteredBy:]
- -[SHClusterController affinityGroupsFromQueryCollection:filteredBySeedCollection:completionHandler:]
- -[SHClusterController dataStore]
- -[SHClusterController filterQueryCollection:byItemsWithinCluster:]
- -[SHClusterController initWithDataStore:]
- -[SHClusterController mediaItemsForPropertyCollection:completionHandler:]
- -[SHClusterController mediaItemsSimilarToValue:forKey:completionHandler:]
- -[SHClusterController query]
- -[SHClusterController resultsFromQueryBlock:completionHandler:]
- -[SHClusterJSONLReader .cxx_destruct]
- -[SHClusterJSONLReader callback]
- -[SHClusterJSONLReader importClusters:toParentCluster:startIndex:]
- -[SHClusterJSONLReader index]
- -[SHClusterJSONLReader parsedJSONObject:error:]
- -[SHClusterJSONLReader readDataLineByLineFromURL:error:callback:]
- -[SHClusterJSONLReader setCallback:]
- -[SHClusterJSONLReader setIndex:]
- -[SHClusterLoader .cxx_destruct]
- -[SHClusterLoader dataFetcher]
- -[SHClusterLoader dataStore]
- -[SHClusterLoader initWithDataFetcher:dataStore:]
- -[SHClusterLoader loadFromURL:type:storefront:reuseExistingData:completion:]
- -[SHClusterLoaderRequest .cxx_destruct]
- -[SHClusterLoaderRequest initWithType:configuration:]
- -[SHClusterLoaderRequest initWithType:sourceURL:outputURL:configuration:]
- -[SHClusterLoaderRequest outputURL]
- -[SHClusterLoaderRequest shouldDeleteExistingDatabaseAtOutputURL]
- -[SHClusterLoaderRequest sourceURLForRequestForStorefront:configuration:completion:]
- -[SHClusterLoaderRequest sourceURL]
- -[SHClusterLoaderRequest type]
- -[SHClusterMetadata .cxx_destruct]
- -[SHClusterMetadata clusterType]
- -[SHClusterMetadata creationDate]
- -[SHClusterMetadata initWithType:storefront:uniqueHash:creationDate:]
- -[SHClusterMetadata storefront]
- -[SHClusterMetadata uniqueHash]
- -[SHClusterQuery .cxx_destruct]
- -[SHClusterQuery configuration]
- -[SHClusterQuery controllerForType:withCompletionHandler:]
- -[SHClusterQuery destinationURL]
- -[SHClusterQuery filterMediaItemQueryCollection:bySeedCollection:completionHandler:]
- -[SHClusterQuery initWithType:configuration:sourceURL:destinationURL:]
- -[SHClusterQuery initWithType:sourceURL:destinationURL:]
- -[SHClusterQuery mediaItemsMatchingValuesInCollection:completionHandler:]
- -[SHClusterQuery mediaItemsWithHighCohesionToValue:forProperty:completionHandler:]
- -[SHClusterQuery sourceURL]
- -[SHClusterQuery statusWithCompletionHandler:]
- -[SHClusterQuery storefront]
- -[SHClusterQuery type]
- -[SHClusterSQLiteDataStore .cxx_destruct]
- -[SHClusterSQLiteDataStore clusterType]
- -[SHClusterSQLiteDataStore dataStatus]
- -[SHClusterSQLiteDataStore databaseFilePathURL]
- -[SHClusterSQLiteDataStore databaseMaxAge]
- -[SHClusterSQLiteDataStore hasNotPassedExpiryDate:isForCountryCode:]
- -[SHClusterSQLiteDataStore initWithClusterType:databaseMaxAge:forStorefront:databaseFilePathURL:]
- -[SHClusterSQLiteDataStore isDataLoaded]
- -[SHClusterSQLiteDataStore isDataValid]
- -[SHClusterSQLiteDataStore requiredStorefront]
- -[SHClusterStatementRunner .cxx_destruct]
- -[SHClusterStatementRunner databaseURL]
- -[SHClusterStatementRunner db]
- -[SHClusterStatementRunner dealloc]
- -[SHClusterStatementRunner initWithDatabaseURL:]
- -[SHClusterStatementRunner mediaItemsAtCohesionLevel:forQueryMediaIDs:filteredBySeedMediaIDs:error:]
- -[SHClusterStatementRunner mediaItemsFromPropertyCollection:error:]
- -[SHClusterStatementRunner mediaItemsSimilarToMediaItemValue:forKey:error:]
- -[SHClusterStatementRunner mediaItemsWithQuery:tokens:objects:error:]
- -[SHClusterStatementRunner supportedKeysForDatabaseAsStringWithPrefix:]
- -[SHClusterStatementRunner supportedKeysForDatabaseAsString]
- -[SHClusterStatementRunner supportedKeysForDatabase]
- -[SHClusterStatementRunner validDatabaseKeys]
- -[SHClusterStatus .cxx_destruct]
- -[SHClusterStatus clusterType]
- -[SHClusterStatus creationDate]
- -[SHClusterStatus dataURL]
- -[SHClusterStatus isDataValid]
- -[SHClusterStatus loadStatus]
- -[SHClusterStatus metadata]
- -[SHClusterStatus setDataURL:]
- -[SHClusterStatus setIsDataValid:]
- -[SHClusterStatus setLoadStatus:]
- -[SHClusterStatus setMetadata:]
- -[SHClusterStatus storefront]
- -[SHClusterStatus uniqueHash]
- -[SHJSONLClusterImporter createTables:error:]
- -[SHJSONLClusterImporter insert:appleMusicID:cohesionID:]
- -[SHJSONLClusterImporter insert:low:medium:high:]
- -[SHJSONLClusterImporter loadDataFromFileInfo:withMetadata:toDestinationURL:error:]
- -[SHLocalDataFetcher fetchClusterURL:forCurrentStorefront:cachedUniqueHash:completionHandler:]
- -[SHMediaItemPropertyCollection .cxx_destruct]
- -[SHMediaItemPropertyCollection collection]
- -[SHMediaItemPropertyCollection initWithArray:representingProperty:]
- -[SHMediaItemPropertyCollection property]
- -[SHSQLiteClusterImporter loadDataFromFileInfo:withMetadata:toDestinationURL:error:]
- GCC_except_table11
- GCC_except_table3
- GCC_except_table4
- GCC_except_table5
- _CC_SHA1_Final
- _CC_SHA1_Init
- _CC_SHA1_Update
- _NSLocalizedFailureErrorKey
- _NSSearchPathForDirectoriesInDomains
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSFileHandle
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSISO8601DateFormatter
- _OBJC_CLASS_$_NSMutableSet
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$_SHClusterController
- _OBJC_CLASS_$_SHClusterImporterUtils
- _OBJC_CLASS_$_SHClusterJSONLReader
- _OBJC_CLASS_$_SHClusterLoader
- _OBJC_CLASS_$_SHClusterLoaderRequest
- _OBJC_CLASS_$_SHClusterMetadata
- _OBJC_CLASS_$_SHClusterMetadataQuery
- _OBJC_CLASS_$_SHClusterQuery
- _OBJC_CLASS_$_SHClusterSQLiteDataStore
- _OBJC_CLASS_$_SHClusterStatementRunner
- _OBJC_CLASS_$_SHClusterStatus
- _OBJC_CLASS_$_SHFileChecksum
- _OBJC_CLASS_$_SHJSONLClusterImporter
- _OBJC_CLASS_$_SHJSONLFileReader
- _OBJC_CLASS_$_SHMediaItemPropertyCollection
- _OBJC_CLASS_$_SHSQLiteClusterImporter
- _OBJC_CLASS_$_SHSQLiteUtils
- _OBJC_CLASS_$_SHStorefront
- _OBJC_IVAR_$_SHClusterController._dataStore
- _OBJC_IVAR_$_SHClusterController._query
- _OBJC_IVAR_$_SHClusterJSONLReader._callback
- _OBJC_IVAR_$_SHClusterJSONLReader._index
- _OBJC_IVAR_$_SHClusterLoader._dataFetcher
- _OBJC_IVAR_$_SHClusterLoader._dataStore
- _OBJC_IVAR_$_SHClusterLoaderRequest._outputURL
- _OBJC_IVAR_$_SHClusterLoaderRequest._sourceURL
- _OBJC_IVAR_$_SHClusterLoaderRequest._type
- _OBJC_IVAR_$_SHClusterMetadata._clusterType
- _OBJC_IVAR_$_SHClusterMetadata._creationDate
- _OBJC_IVAR_$_SHClusterMetadata._storefront
- _OBJC_IVAR_$_SHClusterMetadata._uniqueHash
- _OBJC_IVAR_$_SHClusterQuery._configuration
- _OBJC_IVAR_$_SHClusterQuery._destinationURL
- _OBJC_IVAR_$_SHClusterQuery._sourceURL
- _OBJC_IVAR_$_SHClusterQuery._storefront
- _OBJC_IVAR_$_SHClusterQuery._type
- _OBJC_IVAR_$_SHClusterSQLiteDataStore._clusterType
- _OBJC_IVAR_$_SHClusterSQLiteDataStore._databaseFilePathURL
- _OBJC_IVAR_$_SHClusterSQLiteDataStore._databaseMaxAge
- _OBJC_IVAR_$_SHClusterSQLiteDataStore._requiredStorefront
- _OBJC_IVAR_$_SHClusterStatementRunner._databaseURL
- _OBJC_IVAR_$_SHClusterStatementRunner._db
- _OBJC_IVAR_$_SHClusterStatementRunner._validDatabaseKeys
- _OBJC_IVAR_$_SHClusterStatus._dataURL
- _OBJC_IVAR_$_SHClusterStatus._isDataValid
- _OBJC_IVAR_$_SHClusterStatus._loadStatus
- _OBJC_IVAR_$_SHClusterStatus._metadata
- _OBJC_IVAR_$_SHMediaItemPropertyCollection._collection
- _OBJC_IVAR_$_SHMediaItemPropertyCollection._property
- _OBJC_METACLASS_$_SHClusterController
- _OBJC_METACLASS_$_SHClusterImporterUtils
- _OBJC_METACLASS_$_SHClusterJSONLReader
- _OBJC_METACLASS_$_SHClusterLoader
- _OBJC_METACLASS_$_SHClusterLoaderRequest
- _OBJC_METACLASS_$_SHClusterMetadata
- _OBJC_METACLASS_$_SHClusterMetadataQuery
- _OBJC_METACLASS_$_SHClusterQuery
- _OBJC_METACLASS_$_SHClusterSQLiteDataStore
- _OBJC_METACLASS_$_SHClusterStatementRunner
- _OBJC_METACLASS_$_SHClusterStatus
- _OBJC_METACLASS_$_SHFileChecksum
- _OBJC_METACLASS_$_SHJSONLClusterImporter
- _OBJC_METACLASS_$_SHMediaItemPropertyCollection
- _OBJC_METACLASS_$_SHSQLiteClusterImporter
- _OBJC_METACLASS_$_SHSQLiteUtils
- _SHInsightsCustomCollation
- _SHInsightsDataFetcherErrorDomain
- _SHMediaItemArtist
- _SHMediaItemTitle
- __Block_object_dispose
- __OBJC_$_CLASS_METHODS_SHClusterController
- __OBJC_$_CLASS_METHODS_SHClusterImporterUtils
- __OBJC_$_CLASS_METHODS_SHClusterLoader
- __OBJC_$_CLASS_METHODS_SHClusterMetadataQuery
- __OBJC_$_CLASS_METHODS_SHClusterQuery
- __OBJC_$_CLASS_METHODS_SHClusterSQLiteDataStore
- __OBJC_$_CLASS_METHODS_SHClusterStatementRunner
- __OBJC_$_CLASS_METHODS_SHFileChecksum
- __OBJC_$_CLASS_METHODS_SHMediaItemPropertyCollection
- __OBJC_$_CLASS_METHODS_SHSQLiteUtils
- __OBJC_$_INSTANCE_METHODS_SHClusterController
- __OBJC_$_INSTANCE_METHODS_SHClusterJSONLReader
- __OBJC_$_INSTANCE_METHODS_SHClusterLoader
- __OBJC_$_INSTANCE_METHODS_SHClusterLoaderRequest
- __OBJC_$_INSTANCE_METHODS_SHClusterMetadata
- __OBJC_$_INSTANCE_METHODS_SHClusterQuery
- __OBJC_$_INSTANCE_METHODS_SHClusterSQLiteDataStore
- __OBJC_$_INSTANCE_METHODS_SHClusterStatementRunner
- __OBJC_$_INSTANCE_METHODS_SHClusterStatus
- __OBJC_$_INSTANCE_METHODS_SHJSONLClusterImporter
- __OBJC_$_INSTANCE_METHODS_SHMediaItemPropertyCollection
- __OBJC_$_INSTANCE_METHODS_SHSQLiteClusterImporter
- __OBJC_$_INSTANCE_VARIABLES_SHClusterController
- __OBJC_$_INSTANCE_VARIABLES_SHClusterJSONLReader
- __OBJC_$_INSTANCE_VARIABLES_SHClusterLoader
- __OBJC_$_INSTANCE_VARIABLES_SHClusterLoaderRequest
- __OBJC_$_INSTANCE_VARIABLES_SHClusterMetadata
- __OBJC_$_INSTANCE_VARIABLES_SHClusterQuery
- __OBJC_$_INSTANCE_VARIABLES_SHClusterSQLiteDataStore
- __OBJC_$_INSTANCE_VARIABLES_SHClusterStatementRunner
- __OBJC_$_INSTANCE_VARIABLES_SHClusterStatus
- __OBJC_$_INSTANCE_VARIABLES_SHMediaItemPropertyCollection
- __OBJC_$_PROP_LIST_SHClusterController
- __OBJC_$_PROP_LIST_SHClusterJSONLReader
- __OBJC_$_PROP_LIST_SHClusterLoader
- __OBJC_$_PROP_LIST_SHClusterLoaderRequest
- __OBJC_$_PROP_LIST_SHClusterMetadata
- __OBJC_$_PROP_LIST_SHClusterQuery
- __OBJC_$_PROP_LIST_SHClusterSQLiteDataStore
- __OBJC_$_PROP_LIST_SHClusterStatementRunner
- __OBJC_$_PROP_LIST_SHClusterStatus
- __OBJC_$_PROP_LIST_SHJSONLClusterImporter
- __OBJC_$_PROP_LIST_SHMediaItemPropertyCollection
- __OBJC_$_PROP_LIST_SHSQLiteClusterImporter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHClusterImporter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHJSONLDataDetokenizerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SHClusterImporter
- __OBJC_$_PROTOCOL_METHOD_TYPES_SHJSONLDataDetokenizerDelegate
- __OBJC_$_PROTOCOL_REFS_SHClusterImporter
- __OBJC_$_PROTOCOL_REFS_SHJSONLDataDetokenizerDelegate
- __OBJC_CLASS_PROTOCOLS_$_SHClusterJSONLReader
- __OBJC_CLASS_PROTOCOLS_$_SHJSONLClusterImporter
- __OBJC_CLASS_PROTOCOLS_$_SHSQLiteClusterImporter
- __OBJC_CLASS_RO_$_SHClusterController
- __OBJC_CLASS_RO_$_SHClusterImporterUtils
- __OBJC_CLASS_RO_$_SHClusterJSONLReader
- __OBJC_CLASS_RO_$_SHClusterLoader
- __OBJC_CLASS_RO_$_SHClusterLoaderRequest
- __OBJC_CLASS_RO_$_SHClusterMetadata
- __OBJC_CLASS_RO_$_SHClusterMetadataQuery
- __OBJC_CLASS_RO_$_SHClusterQuery
- __OBJC_CLASS_RO_$_SHClusterSQLiteDataStore
- __OBJC_CLASS_RO_$_SHClusterStatementRunner
- __OBJC_CLASS_RO_$_SHClusterStatus
- __OBJC_CLASS_RO_$_SHFileChecksum
- __OBJC_CLASS_RO_$_SHJSONLClusterImporter
- __OBJC_CLASS_RO_$_SHMediaItemPropertyCollection
- __OBJC_CLASS_RO_$_SHSQLiteClusterImporter
- __OBJC_CLASS_RO_$_SHSQLiteUtils
- __OBJC_LABEL_PROTOCOL_$_SHClusterImporter
- __OBJC_LABEL_PROTOCOL_$_SHJSONLDataDetokenizerDelegate
- __OBJC_METACLASS_RO_$_SHClusterController
- __OBJC_METACLASS_RO_$_SHClusterImporterUtils
- __OBJC_METACLASS_RO_$_SHClusterJSONLReader
- __OBJC_METACLASS_RO_$_SHClusterLoader
- __OBJC_METACLASS_RO_$_SHClusterLoaderRequest
- __OBJC_METACLASS_RO_$_SHClusterMetadata
- __OBJC_METACLASS_RO_$_SHClusterMetadataQuery
- __OBJC_METACLASS_RO_$_SHClusterQuery
- __OBJC_METACLASS_RO_$_SHClusterSQLiteDataStore
- __OBJC_METACLASS_RO_$_SHClusterStatementRunner
- __OBJC_METACLASS_RO_$_SHClusterStatus
- __OBJC_METACLASS_RO_$_SHFileChecksum
- __OBJC_METACLASS_RO_$_SHJSONLClusterImporter
- __OBJC_METACLASS_RO_$_SHMediaItemPropertyCollection
- __OBJC_METACLASS_RO_$_SHSQLiteClusterImporter
- __OBJC_METACLASS_RO_$_SHSQLiteUtils
- __OBJC_PROTOCOL_$_SHClusterImporter
- __OBJC_PROTOCOL_$_SHJSONLDataDetokenizerDelegate
- __Unwind_Resume
- ___100-[SHClusterStatementRunner mediaItemsAtCohesionLevel:forQueryMediaIDs:filteredBySeedMediaIDs:error:]_block_invoke
- ___31+[SHClusterQuery tracksCluster]_block_invoke
- ___32+[SHClusterQuery artistsCluster]_block_invoke
- ___43+[SHSQLiteUtils defenseAgainstBadDatabase:]_block_invoke
- ___46-[SHClusterQuery statusWithCompletionHandler:]_block_invoke
- ___46-[SHClusterQuery statusWithCompletionHandler:]_block_invoke_2
- ___46-[SHClusterQuery statusWithCompletionHandler:]_block_invoke_3
- ___49+[SHSQLiteUtils runNoResultSQL:onDatabase:error:]_block_invoke
- ___50+[SHSQLiteUtils database:hasPopulatedTable:error:]_block_invoke
- ___52-[SHClusterStatementRunner supportedKeysForDatabase]_block_invoke
- ___58-[SHClusterQuery controllerForType:withCompletionHandler:]_block_invoke
- ___58-[SHClusterQuery controllerForType:withCompletionHandler:]_block_invoke_2
- ___63+[SHClusterMetadataQuery metadataFromDatabaseAtLocation:error:]_block_invoke
- ___69-[SHClusterStatementRunner mediaItemsWithQuery:tokens:objects:error:]_block_invoke
- ___73-[SHClusterQuery mediaItemsMatchingValuesInCollection:completionHandler:]_block_invoke
- ___76-[SHClusterLoader loadFromURL:type:storefront:reuseExistingData:completion:]_block_invoke
- ___81+[SHClusterLoader loadDataForRequest:storefront:configuration:completionHandler:]_block_invoke
- ___81+[SHClusterLoader loadDataForRequest:storefront:configuration:completionHandler:]_block_invoke_2
- ___82-[SHClusterQuery mediaItemsWithHighCohesionToValue:forProperty:completionHandler:]_block_invoke
- ___83-[SHJSONLClusterImporter loadDataFromFileInfo:withMetadata:toDestinationURL:error:]_block_invoke
- ___84-[SHClusterLoaderRequest sourceURLForRequestForStorefront:configuration:completion:]_block_invoke
- ___84-[SHClusterLoaderRequest sourceURLForRequestForStorefront:configuration:completion:]_block_invoke_2
- ___84-[SHClusterLoaderRequest sourceURLForRequestForStorefront:configuration:completion:]_block_invoke_3
- ___84-[SHClusterLoaderRequest sourceURLForRequestForStorefront:configuration:completion:]_block_invoke_4
- ___84-[SHClusterQuery filterMediaItemQueryCollection:bySeedCollection:completionHandler:]_block_invoke
- ___92-[SHCDNDataFetcher fetchClusterURL:forCurrentStorefront:cachedUniqueHash:completionHandler:]_block_invoke
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___NSArray0__struct
- ___block_descriptor_32_e23_v16?0^{sqlite3_stmt=}8l
- ___block_descriptor_40_e8_32bs_e46_v24?0"SHClusterSQLiteDataStore"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32r_e23_v16?0^{sqlite3_stmt=}8lr32l8
- ___block_descriptor_40_e8_32s_e23_v16?0^{sqlite3_stmt=}8ls32l8
- ___block_descriptor_48_e8_32r_e23_v16?0^{sqlite3_stmt=}8lr32l8
- ___block_descriptor_48_e8_32s40bs_e41_v24?0"SHClusterController"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e43_v40?0"NSURL"8"NSString"16d24"NSError"32ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e23_v16?0^{sqlite3_stmt=}8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e56_v40?0"NSString"8"NSString"16"NSString"24"NSArray"32ls32l8
- ___block_descriptor_56_e8_32s40bs_e18_v16?0"NSString"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e18_v16?0"NSString"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e41_v24?0"SHClusterController"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v16?0d8ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40bs48w_e43_v24?0"SHDataFetcherFileInfo"8"NSError"16lw48l8s40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v16?0d8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e49_v32?0"NSHTTPURLResponse"8"NSURL"16"NSError"24ls32l8s40l8s64l8s48l8s56l8
- ___block_literal_global.2
- ___objc_personality_v0
- _artistsCluster.artistCluster
- _artistsCluster.onceToken
- _dateFormatter._dateFormatter
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSend$URLByAppendingPathComponent:
- _objc_msgSend$URLByAppendingPathExtension:
- _objc_msgSend$URLByDeletingLastPathComponent
- _objc_msgSend$UUID
- _objc_msgSend$UUIDString
- _objc_msgSend$absoluteString
- _objc_msgSend$addValue:forHTTPHeaderField:
- _objc_msgSend$affinityGroupsAtCohesionLevel:forQuery:queryCollection:filteredBy:
- _objc_msgSend$affinityGroupsFromQueryCollection:filteredBySeedCollection:completionHandler:
- _objc_msgSend$allHeaderFields
- _objc_msgSend$allObjects
- _objc_msgSend$appendFormat:
- _objc_msgSend$appendString:
- _objc_msgSend$appleMusicID
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$artistClusterDefaultLocationURL
- _objc_msgSend$artistsCachedDataMaxAgeWithCompletionHandler:
- _objc_msgSend$artistsCluster
- _objc_msgSend$artistsClusterEndpointWithCompletionHandler:
- _objc_msgSend$base64EncodedStringWithOptions:
- _objc_msgSend$buildTemporaryClusterURLWithError:
- _objc_msgSend$bytes
- _objc_msgSend$cStringUsingEncoding:
- _objc_msgSend$cachesDirectory
- _objc_msgSend$callback
- _objc_msgSend$checksumDataForFile:withError:
- _objc_msgSend$checksumForFile:withError:
- _objc_msgSend$clearTemporaryDatabaseFileAtURL:withError:
- _objc_msgSend$closeAndReturnError:
- _objc_msgSend$closeDatabase:error:
- _objc_msgSend$clusterType
- _objc_msgSend$code
- _objc_msgSend$collection
- _objc_msgSend$commitTransactionOnDatabase:
- _objc_msgSend$compare:options:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$compressionType
- _objc_msgSend$configuration
- _objc_msgSend$controllerForType:withCompletionHandler:
- _objc_msgSend$copyDatabaseFromURL:toDatabaseDestinationURL:error:
- _objc_msgSend$copyItemAtURL:toURL:error:
- _objc_msgSend$createDatabase:atURL:error:
- _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
- _objc_msgSend$createTables:error:
- _objc_msgSend$creationDate
- _objc_msgSend$dataFetcher
- _objc_msgSend$dataStatus
- _objc_msgSend$dataStore
- _objc_msgSend$dataStoreTypeFromString:
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$database:hasPopulatedTable:error:
- _objc_msgSend$databaseFilePathURL
- _objc_msgSend$databaseMaxAge
- _objc_msgSend$databaseURL
- _objc_msgSend$databaseURLForName:
- _objc_msgSend$date
- _objc_msgSend$dateFormatter
- _objc_msgSend$dateFromString:
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$db
- _objc_msgSend$decompressFile:withAlgorithm:toLocation:error:
- _objc_msgSend$defaultManager
- _objc_msgSend$defenseAgainstBadDatabase:
- _objc_msgSend$destinationURL
- _objc_msgSend$doesRequestEtag:matchInResponse:
- _objc_msgSend$domain
- _objc_msgSend$downloadResourceFromRequest:completionHandler:
- _objc_msgSend$fetchClusterURL:forCurrentStorefront:cachedUniqueHash:completionHandler:
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$fileHandleForReadingFromURL:error:
- _objc_msgSend$filterQueryCollection:byItemsWithinCluster:
- _objc_msgSend$firstObject
- _objc_msgSend$hasNotPassedExpiryDate:isForCountryCode:
- _objc_msgSend$importClusters:toParentCluster:startIndex:
- _objc_msgSend$importerForFile:
- _objc_msgSend$index
- _objc_msgSend$initWithArray:representingProperty:
- _objc_msgSend$initWithBytes:length:encoding:
- _objc_msgSend$initWithClusterType:databaseMaxAge:forStorefront:databaseFilePathURL:
- _objc_msgSend$initWithDataFetcher:dataStore:
- _objc_msgSend$initWithDataStore:
- _objc_msgSend$initWithDataURL:
- _objc_msgSend$initWithDatabaseURL:
- _objc_msgSend$initWithType:configuration:
- _objc_msgSend$initWithType:configuration:sourceURL:destinationURL:
- _objc_msgSend$initWithType:sourceURL:destinationURL:
- _objc_msgSend$initWithType:sourceURL:outputURL:configuration:
- _objc_msgSend$initWithType:storefront:uniqueHash:creationDate:
- _objc_msgSend$insert:appleMusicID:cohesionID:
- _objc_msgSend$insert:low:medium:high:
- _objc_msgSend$intValue
- _objc_msgSend$intersectSet:
- _objc_msgSend$isDataLoaded
- _objc_msgSend$isDataValid
- _objc_msgSend$isEqual:
- _objc_msgSend$isEqualToString:
- _objc_msgSend$laterDate:
- _objc_msgSend$loadDataForRequest:storefront:configuration:completionHandler:
- _objc_msgSend$loadDataFromFileInfo:withMetadata:toDestinationURL:error:
- _objc_msgSend$loadDataFromURL:error:
- _objc_msgSend$loadFromURL:type:storefront:reuseExistingData:completion:
- _objc_msgSend$loadStatus
- _objc_msgSend$mediaItems
- _objc_msgSend$mediaItemsAtCohesionLevel:forQueryMediaIDs:filteredBySeedMediaIDs:error:
- _objc_msgSend$mediaItemsForPropertyCollection:completionHandler:
- _objc_msgSend$mediaItemsFromPropertyCollection:error:
- _objc_msgSend$mediaItemsSimilarToMediaItemValue:forKey:error:
- _objc_msgSend$mediaItemsSimilarToValue:forKey:completionHandler:
- _objc_msgSend$mediaItemsWithQuery:tokens:objects:error:
- _objc_msgSend$metadata
- _objc_msgSend$metadataFromDatabaseAtLocation:error:
- _objc_msgSend$mutableCopy
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$openDatabase:atURL:error:
- _objc_msgSend$outputURL
- _objc_msgSend$path
- _objc_msgSend$property
- _objc_msgSend$query
- _objc_msgSend$queryStringForCount:
- _objc_msgSend$readDataLineByLineFromURL:error:callback:
- _objc_msgSend$readDataOfLength:
- _objc_msgSend$removeItemAtURL:error:
- _objc_msgSend$removeObject:
- _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
- _objc_msgSend$requiredStorefront
- _objc_msgSend$runNoResultSQL:onDatabase:error:
- _objc_msgSend$runSQL:onDatabase:replacingTokens:withObjects:rowHandler:error:
- _objc_msgSend$set
- _objc_msgSend$setCallback:
- _objc_msgSend$setDataURL:
- _objc_msgSend$setDelegate:
- _objc_msgSend$setFormatOptions:
- _objc_msgSend$setIndex:
- _objc_msgSend$setIsDataValid:
- _objc_msgSend$setLoadStatus:
- _objc_msgSend$setMetadata:
- _objc_msgSend$setStorefront:
- _objc_msgSend$setWithArray:
- _objc_msgSend$setWithCapacity:
- _objc_msgSend$shouldDeleteExistingDatabaseAtOutputURL
- _objc_msgSend$sourceURL
- _objc_msgSend$sourceURLForRequestForStorefront:configuration:completion:
- _objc_msgSend$sqliteDatabaseExistsAtURL:
- _objc_msgSend$startTransactionOnDatabase:
- _objc_msgSend$storefront
- _objc_msgSend$storefrontCountryCode:
- _objc_msgSend$string
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$stringFromDate:
- _objc_msgSend$stringFromStoreType:
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$stringWithString:
- _objc_msgSend$supportedKeys
- _objc_msgSend$supportedKeysForDatabase
- _objc_msgSend$supportedKeysForDatabaseAsString
- _objc_msgSend$supportedKeysForDatabaseAsStringWithPrefix:
- _objc_msgSend$trackClusterDefaultLocationURL
- _objc_msgSend$tracksCachedDataMaxAgeWithCompletionHandler:
- _objc_msgSend$tracksCluster
- _objc_msgSend$tracksClusterEndpointForStorefront:completionHandler:
- _objc_msgSend$type
- _objc_msgSend$uniqueHash
- _objc_msgSend$validDatabaseKeys
- _objc_msgSend$writeMetadata:toDatabaseAtLocation:error:
- _objc_release_x27
- _objc_release_x9
- _objc_retain_x25
- _sh_CaseDiacriticInsensitiveCollation
- _sh_columnToText
- _sh_databaseErrorToNSError
- _sh_log_object
- _sqlite3_bind_int
- _sqlite3_bind_int64
- _sqlite3_bind_text
- _sqlite3_close
- _sqlite3_column_int
- _sqlite3_column_text
- _sqlite3_create_collation
- _sqlite3_db_config
- _sqlite3_errmsg
- _sqlite3_exec
- _sqlite3_finalize
- _sqlite3_open
- _sqlite3_open_v2
- _sqlite3_prepare_v2
- _sqlite3_step
- _tracksCluster.onceToken
- _tracksCluster.trackCluster
CStrings:
- ""
- " "
- " AND s1.high = c1.high AND s1.medium = c1.medium"
- " AND s1.medium = c1.medium"
- " where t1.%@ in (<QUERY_MEDIA_IDS>) AND t1.cohesion = c1.id order by %@"
- "\""
- "%@"
- "%@_temp"
- "%lu%@"
- ", "
- ", ?"
- "<MEDIA_IDS>"
- "<MEDIA_NAME2>"
- "<MEDIA_NAME>"
- "<QUERY_MEDIA_IDS>"
- "<SEED_MEDIA_IDS>"
- "?"
- "@\"NSSet\""
- "@\"SHClusterMetadata\""
- "@\"SHClusterSQLiteDataStore\""
- "@\"SHClusterStatementRunner\""
- "@\"SHInsightsConfiguration\""
- "@\"SHStorefront\""
- "@24@0:8^@16"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32^@40"
- "@48@0:8q16@24@32@40"
- "@48@0:8q16@24@32^@40"
- "@48@0:8q16d24@32@40"
- "@?"
- "@?16@0:8"
- "B"
- "B24@0:8^{sqlite3=}16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8^{sqlite3=}16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16^@24@?32"
- "B40@0:8@16^{sqlite3=}24^@32"
- "B40@0:8^^{sqlite3}16@24^@32"
- "B40@0:8^{sqlite3=}16@24^@32"
- "B40@0:8^{sqlite3=}16@24q32"
- "B48@0:8@\"SHDataFetcherFileInfo\"16@\"SHClusterMetadata\"24@\"NSURL\"32^@40"
- "B48@0:8@16@24@32^@40"
- "B64@0:8@16^{sqlite3=}24@32@40@?48^@56"
- "BEGIN"
- "COMMIT"
- "CREATE TABLE if not exists Cohesion(id INTEGER PRIMARY KEY, high INTEGER, medium INTEGER, low INTEGER, CONSTRAINT constraint_name UNIQUE(low, medium, high) ON CONFLICT IGNORE)"
- "CREATE TABLE if not exists MediaItems(sh_appleMusicID VARCHAR, cohesion INTEGER, FOREIGN KEY(cohesion) REFERENCES Cohesion(id))"
- "CREATE TABLE if not exists Metadata(type VARCHAR, hash VARCHAR, storefront VARCHAR, creationDate DATE)"
- "Cluster data already loaded"
- "Cohesion"
- "Error reading metadata %@"
- "Error updating metadata %@"
- "Etag missing for request to %@, replacing with random hash"
- "Failed get a trackID from tracks query"
- "Failed to check database load status %@"
- "Failed to create the caches directory!"
- "Failed to delete existing database %@"
- "Failed to load the datastore %@"
- "Failed to move database into place %@"
- "Failed to open database for artist query %@"
- "Failed to open database for metadata with error %@"
- "Failed to perform artists query %@"
- "Failed to query database %@"
- "Failed to read the database metadata"
- "Failed to run quick check %@"
- "Failed to turn on cell_size_check %@"
- "INSERT INTO Cohesion (low, medium, high) VALUES (?, ?, ?) returning id"
- "INSERT INTO MediaItems (sh_appleMusicID, cohesion) VALUES (?, ?);"
- "INSERT into Metadata(type, hash, storefront, creationDate) VALUES(?,?,?,?)"
- "INSIGHTS_CUSTOM"
- "If-None-Match"
- "Metadata"
- "PRAGMA cell_size_check=ON"
- "PRAGMA quick_check"
- "PRAGMA table_info('MediaItems')"
- "Q"
- "SELECT COUNT(*) FROM %@"
- "SHClusterController"
- "SHClusterImporter"
- "SHClusterImporterUtils"
- "SHClusterJSONLReader"
- "SHClusterLoader"
- "SHClusterLoaderRequest"
- "SHClusterMetadata"
- "SHClusterMetadataQuery"
- "SHClusterQuery"
- "SHClusterSQLiteDataStore"
- "SHClusterStatementRunner"
- "SHClusterStatus"
- "SHFileChecksum"
- "SHJSONLClusterImporter"
- "SHJSONLDataDetokenizerDelegate"
- "SHMediaItemPropertyCollection"
- "SHSQLiteClusterImporter"
- "SHSQLiteUtils"
- "T@\"NSArray\",R,N,V_validDatabaseKeys"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSSet\",R,N,V_collection"
- "T@\"NSString\",R,C,N,V_requiredStorefront"
- "T@\"NSString\",R,C,N,V_storefront"
- "T@\"NSString\",R,C,N,V_uniqueHash"
- "T@\"NSString\",R,N,V_property"
- "T@\"NSURL\",&,N,V_dataURL"
- "T@\"NSURL\",R,N,V_databaseFilePathURL"
- "T@\"NSURL\",R,N,V_databaseURL"
- "T@\"NSURL\",R,N,V_destinationURL"
- "T@\"NSURL\",R,N,V_outputURL"
- "T@\"NSURL\",R,N,V_sourceURL"
- "T@\"SHClusterMetadata\",&,N,V_metadata"
- "T@\"SHClusterSQLiteDataStore\",R,N,V_dataStore"
- "T@\"SHClusterStatementRunner\",R,N,V_query"
- "T@\"SHClusterStatus\",R,N"
- "T@\"SHInsightsConfiguration\",R,N,V_configuration"
- "T@\"SHStorefront\",R,N,V_storefront"
- "T@?,C,N,V_callback"
- "TB,N,V_isDataValid"
- "TB,R,N"
- "TQ,N,V_index"
- "T^{sqlite3=},R,N,V_db"
- "Td,R,N,V_databaseMaxAge"
- "Tq,N,V_loadStatus"
- "Tq,R,N"
- "Tq,R,N,V_clusterType"
- "Tq,R,N,V_type"
- "UPDATE Metadata set type = ?, hash = ?, storefront = ?, creationDate = ?"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "URLByDeletingLastPathComponent"
- "UUID"
- "UUIDString"
- "Unknown Error"
- "Unknown database type %@, assuming it is tracks"
- "Unreadable metadata, failing"
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "_callback"
- "_clusterType"
- "_collection"
- "_configuration"
- "_dataStore"
- "_dataURL"
- "_databaseFilePathURL"
- "_databaseMaxAge"
- "_databaseURL"
- "_db"
- "_destinationURL"
- "_index"
- "_isDataValid"
- "_loadStatus"
- "_metadata"
- "_outputURL"
- "_property"
- "_query"
- "_requiredStorefront"
- "_sourceURL"
- "_type"
- "_validDatabaseKeys"
- "absoluteString"
- "addValue:forHTTPHeaderField:"
- "affinityGroupsAtCohesionLevel:forQuery:queryCollection:filteredBy:"
- "affinityGroupsFromQueryCollection:filteredBySeedCollection:completionHandler:"
- "allHeaderFields"
- "allObjects"
- "appendFormat:"
- "appendString:"
- "appleMusicID"
- "arrayWithObjects:count:"
- "artistClusterDefaultLocationURL"
- "artists"
- "artistsCluster"
- "base64EncodedStringWithOptions:"
- "buildTemporaryClusterURLWithError:"
- "bytes"
- "cStringUsingEncoding:"
- "cachesDirectory"
- "callback"
- "checksumDataForFile:withError:"
- "checksumForFile:withError:"
- "clearTemporaryDatabaseFileAtURL:withError:"
- "closeAndReturnError:"
- "closeDatabase:error:"
- "clusterForType:"
- "clusterType"
- "clusters"
- "code"
- "collection"
- "collectionWithArray:representingProperty:"
- "com.apple.ShazamInsightsDataFetcher"
- "commitTransactionOnDatabase:"
- "compare:options:"
- "componentsSeparatedByString:"
- "configuration"
- "controllerForType:withCompletionHandler:"
- "copyDatabaseFromURL:toDatabaseDestinationURL:error:"
- "copyItemAtURL:toURL:error:"
- "createDatabase:atURL:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createTables:error:"
- "d"
- "d16@0:8"
- "dataStatus"
- "dataStore"
- "dataStoreTypeFromString:"
- "dataURL"
- "dataWithBytes:length:"
- "database:hasPopulatedTable:error:"
- "databaseFilePathURL"
- "databaseMaxAge"
- "databaseURL"
- "databaseURLForName:"
- "date"
- "dateFormatter"
- "dateFromString:"
- "dateWithTimeIntervalSinceNow:"
- "db"
- "dealloc"
- "decompressFile:withAlgorithm:toLocation:error:"
- "defaultManager"
- "defenseAgainstBadDatabase:"
- "destinationURL"
- "doesRequestEtag:matchInResponse:"
- "domain"
- "fetchClusterURL:forCurrentStorefront:cachedUniqueHash:completionHandler:"
- "fileExistsAtPath:"
- "fileHandleForReadingFromURL:error:"
- "filterMediaItemQueryCollection:bySeedCollection:completionHandler:"
- "filterQueryCollection:byItemsWithinCluster:"
- "firstObject"
- "hasNotPassedExpiryDate:isForCountryCode:"
- "importClusters:toParentCluster:startIndex:"
- "importerForFile:"
- "index"
- "initWithArray:representingProperty:"
- "initWithBytes:length:encoding:"
- "initWithClusterType:databaseMaxAge:forStorefront:databaseFilePathURL:"
- "initWithDataFetcher:dataStore:"
- "initWithDataStore:"
- "initWithDatabaseURL:"
- "initWithType:configuration:"
- "initWithType:configuration:sourceURL:destinationURL:"
- "initWithType:sourceURL:destinationURL:"
- "initWithType:sourceURL:outputURL:configuration:"
- "initWithType:storefront:uniqueHash:creationDate:"
- "insert:appleMusicID:cohesionID:"
- "insert:low:medium:high:"
- "intValue"
- "intersectSet:"
- "isDataLoaded"
- "isDataValid"
- "isEqualToString:"
- "laterDate:"
- "loadDataForRequest:storefront:configuration:completionHandler:"
- "loadDataFromFileInfo:withMetadata:toDestinationURL:error:"
- "loadDataFromURL:error:"
- "loadFromURL:type:storefront:reuseExistingData:completion:"
- "loadStatus"
- "mediaItemsAtCohesionLevel:forQueryMediaIDs:filteredBySeedMediaIDs:error:"
- "mediaItemsForPropertyCollection:completionHandler:"
- "mediaItemsFromPropertyCollection:error:"
- "mediaItemsMatchingValuesInCollection:completionHandler:"
- "mediaItemsSimilarToMediaItemValue:forKey:error:"
- "mediaItemsSimilarToValue:forKey:completionHandler:"
- "mediaItemsWithHighCohesionToValue:forProperty:completionHandler:"
- "mediaItemsWithQuery:tokens:objects:error:"
- "metadata"
- "metadataFromDatabaseAtLocation:error:"
- "mutableCopy"
- "objectAtIndexedSubscript:"
- "ok"
- "openDatabase:atURL:error:"
- "outputURL"
- "parsedJSONObject:error:"
- "path"
- "property"
- "q24@0:8@16"
- "q36@0:8^{sqlite3=}16i24i28i32"
- "query"
- "queryStringForCount:"
- "readDataLineByLineFromURL:error:callback:"
- "readDataOfLength:"
- "removeItemAtURL:error:"
- "removeObject:"
- "replaceOccurrencesOfString:withString:options:range:"
- "requiredStorefront"
- "resultsFromQueryBlock:completionHandler:"
- "runNoResultSQL:onDatabase:error:"
- "runSQL:onDatabase:replacingTokens:withObjects:rowHandler:error:"
- "select %@ from MediaItems t1, Cohesion c1 INNER JOIN (select  c2.high, c2.medium, c2.low from MediaItems t2, Cohesion c2 where t2.%@ in (<SEED_MEDIA_IDS>) AND t2.cohesion = c2.id order by %@) as s1 ON s1.low = c1.low"
- "select %@ from MediaItems where %@ COLLATE %@ in (<MEDIA_IDS>)"
- "select %@ from MediaItems where cohesion = (select cohesion from MediaItems where %@ = <MEDIA_NAME> COLLATE %@) and %@ != <MEDIA_NAME2> COLLATE %@"
- "select type, storefront, hash, creationDate from Metadata LIMIT 1"
- "set"
- "setCallback:"
- "setDataURL:"
- "setDelegate:"
- "setFormatOptions:"
- "setIndex:"
- "setIsDataValid:"
- "setLoadStatus:"
- "setMetadata:"
- "setWithArray:"
- "setWithCapacity:"
- "shouldDeleteExistingDatabaseAtOutputURL"
- "sourceURL"
- "sourceURLForRequestForStorefront:configuration:completion:"
- "sqliteDatabaseExistsAtURL:"
- "startTransactionOnDatabase:"
- "statusWithCompletionHandler:"
- "storefrontCountryCode:"
- "string"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringFromDate:"
- "stringFromStoreType:"
- "stringWithCString:encoding:"
- "stringWithString:"
- "supportedKeys"
- "supportedKeysForDatabase"
- "supportedKeysForDatabaseAsString"
- "supportedKeysForDatabaseAsStringWithPrefix:"
- "t1."
- "trackClusterDefaultLocationURL"
- "tracks"
- "tracksCluster"
- "type"
- "unknown"
- "v16@?0@\"NSString\"8"
- "v16@?0^{sqlite3_stmt=}8"
- "v16@?0d8"
- "v20@0:8B16"
- "v24@0:8Q16"
- "v24@0:8^{sqlite3=}16"
- "v24@0:8q16"
- "v24@?0@\"SHClusterController\"8@\"NSError\"16"
- "v24@?0@\"SHClusterSQLiteDataStore\"8@\"NSError\"16"
- "v32@0:8@?16@?24"
- "v32@0:8q16@?24"
- "v32@?0@\"NSHTTPURLResponse\"8@\"NSURL\"16@\"NSError\"24"
- "v40@0:8@16@24Q32"
- "v40@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSArray\"32"
- "v40@?0@\"NSURL\"8@\"NSString\"16d24@\"NSError\"32"
- "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"SHDataFetcherFileInfo\"@\"NSError\">40"
- "v52@0:8@16q24@32B40@?44"
- "validDatabaseKeys"
- "writeMetadata:toDatabaseAtLocation:error:"

```
