## WebCore

> `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-619.2.3.1.0
-  __TEXT.__text: 0x2a48418
+619.2.5.10.3
+  __TEXT.__text: 0x2a494c0
   __TEXT.__auth_stubs: 0xc710
   __TEXT.__objc_methlist: 0x49a4
   __TEXT.__const: 0x1a4290
-  __TEXT.__cstring: 0x12f297
-  __TEXT.__gcc_except_tab: 0x208c4
+  __TEXT.__cstring: 0x12f2d7
+  __TEXT.__gcc_except_tab: 0x20904
   __TEXT.__oslogstring: 0xf052
   __TEXT.__ustring: 0x262
-  __TEXT.__unwind_info: 0x1d698
+  __TEXT.__unwind_info: 0x1d6b0
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0xebe
   __TEXT.__objc_methname: 0x119af

   __DATA_CONST.__jsc_ops: 0x4c0
   __AUTH_CONST.__auth_got: 0x63a0
   __AUTH_CONST.__auth_ptr: 0x1a0
-  __AUTH_CONST.__const: 0x25b138
+  __AUTH_CONST.__const: 0x25b170
   __AUTH_CONST.__cfstring: 0x6f60
   __AUTH_CONST.__objc_const: 0x9338
   __AUTH_CONST.__objc_arrayobj: 0x90

   __AUTH.__data: 0xe20
   __DATA.__objc_ivar: 0x464
   __DATA.__data: 0x11c60
-  __DATA.__common: 0x12c08
-  __DATA.__bss: 0x3ebf8
+  __DATA.__common: 0x12bc8
+  __DATA.__bss: 0x3e8f0
   __DATA_DIRTY.__objc_ivar: 0x6c
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x6d40
-  __DATA_DIRTY.__bss: 0x9f49
-  __DATA_DIRTY.__common: 0xa4a9
+  __DATA_DIRTY.__bss: 0xa269
+  __DATA_DIRTY.__common: 0xa501
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore

   - /usr/lib/libxslt.1.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  Functions: 117889
-  Symbols:   123818
+  Functions: 117895
+  Symbols:   123825
   CStrings:  32111
 
Symbols:
+ __ZN7WebCore12IDBIndexInfoC1EyN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS1_6StringEONSt3__17variantIJS7_NS1_6VectorIS7_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEbb
+ __ZNK7WebCore29VideoPresentationInterfaceIOS10logChannelEv
+ __ZN7WebCore4Page37intelligenceTextAnimationsDidCompleteEv
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11renameIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS5_6StringE
+ __ZN7WebCore9IDBClient18IDBConnectionProxy16clearObjectStoreERNS0_20TransactionOperationEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
+ __ZN7WebCore14IDBRequestDataC1EN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS_21IDBResourceIdentifierES7_ONSt3__18optionalIS7_EENS9_INS2_INS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEEEyNS_9IndexedDB15IndexRecordTypeEyNSH_11RequestTypeE
+ __ZN7WebCore18IDBObjectStoreInfoC1EN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS1_6StringEONSt3__18optionalINSA_7variantIJS7_NS1_6VectorIS7_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEEEbONS1_7HashMapIyNS_12IDBIndexInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENSO_ISL_EENS1_15HashTableTraitsEEE
+ __ZN7WebCore14DocumentLoader15setNavigationIDEN3WTF23ObjectIdentifierGenericINS_24NavigationIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEE
+ __ZN7WebCore9IDBClient18IDBConnectionProxy11deleteIndexERNS0_20TransactionOperationEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS4_6StringE
+ __ZNK7WebCore29VideoPresentationInterfaceIOS13logIdentifierEv
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11deleteIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
+ __ZN7WebCore18IDBObjectStoreInfoC2EN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS1_6StringEONSt3__18optionalINSA_7variantIJS7_NS1_6VectorIS7_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEEEbONS1_7HashMapIyNS_12IDBIndexInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENSO_ISL_EENS1_15HashTableTraitsEEE
+ __ZN7WebCore12IDBIndexInfoC2EyN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS1_6StringEONSt3__17variantIJS7_NS1_6VectorIS7_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEbb
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction17renameObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
+ __ZN7WebCore15IDBDatabaseInfoC1ERKN3WTF6StringEyyONS1_7HashMapINS1_23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_18IDBObjectStoreInfoENS1_11DefaultHashISA_EENS1_10HashTraitsISA_EENSE_ISB_EENS1_15HashTableTraitsEEE
+ __ZN7WebCore9IDBServer9IDBServer17renameObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
+ __ZN7WebCore13IDBCursorInfoC2ERKNS_21IDBResourceIdentifierES3_N3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS_15IDBKeyRangeDataENS_9IndexedDB12CursorSourceENSD_15CursorDirectionENSD_10CursorTypeE
+ __ZN7WebCore15IDBDatabaseInfoC2ERKN3WTF6StringEyyONS1_7HashMapINS1_23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEENS_18IDBObjectStoreInfoENS1_11DefaultHashISA_EENS1_10HashTraitsISA_EENSE_ISB_EENS1_15HashTableTraitsEEE
+ __ZN7WebCore9IDBServer9IDBServer11deleteIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS5_6StringE
+ __ZN7WebCore13IDBCursorInfoC1ERKNS_21IDBResourceIdentifierES3_N3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS_15IDBKeyRangeDataENS_9IndexedDB12CursorSourceENSD_15CursorDirectionENSD_10CursorTypeE
+ __ZN7WebCore22EmptyFrameLoaderClient39dispatchDecidePolicyForNavigationActionERKNS_16NavigationActionERKNS_15ResourceRequestERKNS_16ResourceResponseEPNS_9FormStateERKN3WTF6StringENSC_23ObjectIdentifierGenericINS_24NavigationIdentifierTypeENSC_38ObjectIdentifierMainThreadAccessTraitsIyEEyEEONSt3__18optionalINS_13HitTestResultEEEbiNS_18PolicyDecisionModeEONSC_17CompletionHandlerIFvNS_12PolicyActionEEEE
+ __ZN7WebCore9IDBClient18IDBConnectionProxy11renameIndexERNS0_20TransactionOperationEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS4_6StringE
+ __ZN7WebCore9IDBClient18IDBConnectionProxy17renameObjectStoreERNS0_20TransactionOperationEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS4_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEERKNS4_6StringE
+ __ZN7WebCore14IDBRequestDataC2EN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS_21IDBResourceIdentifierES7_ONSt3__18optionalIS7_EENS9_INS2_INS_28IDBObjectStoreIdentifierTypeENS1_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEEEyNS_9IndexedDB15IndexRecordTypeEyNSH_11RequestTypeE
+ __ZN7WebCore9IDBServer9IDBServer11renameIndexERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEEyRKNS5_6StringE
+ __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction16clearObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
+ __ZNK7WebCore29VideoPresentationInterfaceIOS9loggerPtrEv
+ __ZN7WebCore9IDBServer9IDBServer16clearObjectStoreERKNS_14IDBRequestDataEN3WTF23ObjectIdentifierGenericINS_28IDBObjectStoreIdentifierTypeENS5_38ObjectIdentifierThreadSafeAccessTraitsIyEEyEE
- __ZN7WebCore22EmptyFrameLoaderClient39dispatchDecidePolicyForNavigationActionERKNS_16NavigationActionERKNS_15ResourceRequestERKNS_16ResourceResponseEPNS_9FormStateERKN3WTF6StringEyONSt3__18optionalINS_13HitTestResultEEEbiNS_18PolicyDecisionModeEONSC_17CompletionHandlerIFvNS_12PolicyActionEEEE
- __ZN7WebCore15IDBDatabaseInfoC2ERKN3WTF6StringEyyyONS1_7HashMapIyNS_18IDBObjectStoreInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENS9_IS6_EENS1_15HashTableTraitsEEE
- __ZN7WebCore9IDBClient18IDBConnectionProxy16clearObjectStoreERNS0_20TransactionOperationEy
- __ZN7WebCore12IDBIndexInfoC1EyyRKN3WTF6StringEONSt3__17variantIJS2_NS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEbb
- __ZN7WebCore9IDBServer9IDBServer11renameIndexERKNS_14IDBRequestDataEyyRKN3WTF6StringE
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction16clearObjectStoreERKNS_14IDBRequestDataEy
- __ZN7WebCore14IDBRequestDataC2EN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS_21IDBResourceIdentifierES7_ONSt3__18optionalIS7_EEyyNS_9IndexedDB15IndexRecordTypeEyNSC_11RequestTypeE
- __ZN7WebCore12IDBIndexInfoC2Ev
- __ZN7WebCore13IDBCursorInfoC2ERKNS_21IDBResourceIdentifierES3_yyRKNS_15IDBKeyRangeDataENS_9IndexedDB12CursorSourceENS7_15CursorDirectionENS7_10CursorTypeE
- __ZN7WebCore9IDBClient18IDBConnectionProxy11renameIndexERNS0_20TransactionOperationEyyRKN3WTF6StringE
- __ZN7WebCore14DocumentLoader15setNavigationIDEy
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction17renameObjectStoreERKNS_14IDBRequestDataEyRKN3WTF6StringE
- __ZN7WebCore15IDBDatabaseInfoC1ERKN3WTF6StringEyyyONS1_7HashMapIyNS_18IDBObjectStoreInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENS9_IS6_EENS1_15HashTableTraitsEEE
- __ZN7WebCore9IDBClient18IDBConnectionProxy17renameObjectStoreERNS0_20TransactionOperationEyRKN3WTF6StringE
- __ZN7WebCore18IDBObjectStoreInfoC2EyRKN3WTF6StringEONSt3__18optionalINS5_7variantIJS2_NS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEEEbONS1_7HashMapIyNS_12IDBIndexInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENSJ_ISG_EENS1_15HashTableTraitsEEE
- __ZN7WebCore14IDBRequestDataC1EN3WTF23ObjectIdentifierGenericINS_21ProcessIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsIyEEyEENS_21IDBResourceIdentifierES7_ONSt3__18optionalIS7_EEyyNS_9IndexedDB15IndexRecordTypeEyNSC_11RequestTypeE
- __ZN7WebCore9IDBServer9IDBServer16clearObjectStoreERKNS_14IDBRequestDataEy
- __ZN7WebCore12IDBIndexInfoC2EyyRKN3WTF6StringEONSt3__17variantIJS2_NS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEbb
- __ZNK7WebCore4Page41showSelectionForActiveWritingToolsSessionEv
- __ZN7WebCore13IDBCursorInfoC1ERKNS_21IDBResourceIdentifierES3_yyRKNS_15IDBKeyRangeDataENS_9IndexedDB12CursorSourceENS7_15CursorDirectionENS7_10CursorTypeE
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11deleteIndexERKNS_14IDBRequestDataEyRKN3WTF6StringE
- __ZN7WebCore18IDBObjectStoreInfoC1Ev
- __ZN7WebCore9IDBServer28UniqueIDBDatabaseTransaction11renameIndexERKNS_14IDBRequestDataEyyRKN3WTF6StringE
- __ZN7WebCore18IDBObjectStoreInfoC1EyRKN3WTF6StringEONSt3__18optionalINS5_7variantIJS2_NS1_6VectorIS2_Lm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEEEEEEEbONS1_7HashMapIyNS_12IDBIndexInfoENS1_11DefaultHashIyEENS1_10HashTraitsIyEENSJ_ISG_EENS1_15HashTableTraitsEEE
- __ZN7WebCore9IDBServer9IDBServer17renameObjectStoreERKNS_14IDBRequestDataEyRKN3WTF6StringE
- __ZN7WebCore12IDBIndexInfoC1Ev
- __ZN7WebCore9IDBClient18IDBConnectionProxy11deleteIndexERNS0_20TransactionOperationEyRKN3WTF6StringE
- __ZN7WebCore18IDBObjectStoreInfoC2Ev
- __ZN7WebCore9IDBServer9IDBServer11deleteIndexERKNS_14IDBRequestDataEyRKN3WTF6StringE
CStrings:
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
+ "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::keyExistsInObjectStore(const IDBResourceIdentifier &, IDBObjectStoreIdentifier, const IDBKeyData &, bool &)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::revertGeneratedKeyNumber(const IDBResourceIdentifier &, IDBObjectStoreIdentifier, uint64_t)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
+ "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::generateKeyNumber(const IDBResourceIdentifier &, IDBObjectStoreIdentifier, uint64_t &)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExceptionScope.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::maybeUpdateKeyGeneratorNumber(const IDBResourceIdentifier &, IDBObjectStoreIdentifier, double)"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
+ "/AppleInternal/Library/BuildRoots/f3587ae2-763a-11ef-9333-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::keyExistsInObjectStore(const IDBResourceIdentifier &, uint64_t, const IDBKeyData &, bool &)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::generateKeyNumber(const IDBResourceIdentifier &, uint64_t, uint64_t &)"
- "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::maybeUpdateKeyGeneratorNumber(const IDBResourceIdentifier &, uint64_t, double)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
- "virtual IDBError WebCore::IDBServer::MemoryIDBBackingStore::revertGeneratedKeyNumber(const IDBResourceIdentifier &, uint64_t, uint64_t)"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExceptionScope.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"

```
