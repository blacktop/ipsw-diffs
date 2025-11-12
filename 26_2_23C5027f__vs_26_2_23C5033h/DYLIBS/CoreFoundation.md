## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

 4109.1.101.0.0
-  __TEXT.__text: 0x1b72c8
+  __TEXT.__text: 0x1b940c
   __TEXT.__auth_stubs: 0x31d0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x7a5c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 033A9F72-2D89-3EDC-909A-883D4D5D28FE
+  UUID: 03389B6F-DCCD-324D-BFA8-62BD3E110991
   Functions: 7875
   Symbols:   20207
   CStrings:  101739
Functions:
~ -[CFPDSource clearPlist] : 88 -> 84
~ _OUTLINED_FUNCTION_7 : 16 -> 12
~ -[CFPDSource hasObservers] : 68 -> 64
~ -[CFPDSource closeFileDescriptors] : 100 -> 96
~ -[CFPDSource shouldBePurgable] : 92 -> 88
~ -[_CFPrefsSynchronizer synchronize] : 88 -> 96
~ -[_CFPrefsSynchronizer copyDirtySourcesSnapshotAndClear] : 96 -> 92
~ -[_CFPrefsSynchronizer clear_alreadyLocked] : 72 -> 68
~ -[NSMethodSignature _typeString] : 380 -> 400
~ _OUTLINED_FUNCTION_8 : 12 -> 16
~ -[CFPrefsSource copyDictionary] : 72 -> 68
~ -[CFPrefsSearchListSource alreadylocked_requestNewData] : 164 -> 160
~ _CFRunLoopAddSource.cold.1 : 88 -> 80
~ __CFRunLoopRunSpecificWithOptions.cold.1 : 88 -> 80
~ _CFRunLoopWakeUp.cold.1 : 88 -> 80
~ -[_CFXPreferences destroyConnections] : 136 -> 144
~ _CFRunLoopContainsSource.cold.1 : 88 -> 80
~ _CFRunLoopRemoveSource.cold.1 : 88 -> 80
~ -[CFPrefsSource copyKeyList] : 72 -> 68
~ _CFRunLoopPerformBlock.cold.1 : 88 -> 80
~ -[__NSArray0 objectAtIndex:] : 244 -> 264
~ -[__NSOrderedSetI objectAtIndex:] : 500 -> 540
~ -[__NSOrderedSetI getObjects:range:] : 868 -> 948
~ -[__NSOrderedSetI countByEnumeratingWithState:objects:count:] : 524 -> 564
~ -[NSMutableSet addObjects:count:] : 756 -> 816
~ -[NSMutableSet addObjectsFromArray:] : 656 -> 676
~ -[NSMutableSet addObjectsFromOrderedSet:] : 500 -> 520
~ -[NSMutableSet minusOrderedSet:] : 540 -> 560
~ -[NSMutableSet removeObjectsInArray:range:] : 788 -> 848
~ -[NSMutableSet removeObjectsInArray:] : 500 -> 520
~ -[NSMutableSet removeObjectsInOrderedSet:range:] : 788 -> 848
~ -[NSMutableSet removeObjectsInOrderedSet:] : 500 -> 520
~ -[NSMutableSet removeObjectsPassingTest:] : 304 -> 324
~ -[NSMutableSet replaceObject:] : 448 -> 468
~ -[NSMutableSet setObject:] : 448 -> 468
~ -[NSMutableSet setArray:] : 508 -> 528
~ -[NSMutableSet setOrderedSet:] : 548 -> 568
~ -[NSMutableSet unionOrderedSet:] : 540 -> 560
~ -[NSMutableSet initWithObjects:count:] : 772 -> 832
~ -[__NSPlaceholderArray initWithObjects:count:] : 900 -> 960
~ -[__NSPlaceholderArray initWithCapacity:] : 380 -> 400
~ -[__NSPlaceholderArray initWithContentsOfFile:] : 344 -> 364
~ -[__NSPlaceholderArray initWithContentsOfURL:] : 388 -> 408
~ -[NSMutableOrderedSet addObject:] : 380 -> 400
~ -[NSMutableOrderedSet addObjects:count:] : 776 -> 836
~ -[NSMutableOrderedSet addObjectsFromArray:range:] : 792 -> 852
~ -[NSMutableOrderedSet addObjectsFromOrderedSet:range:] : 792 -> 852
~ -[NSMutableOrderedSet addObjectsFromSet:] : 396 -> 416
~ -[NSMutableOrderedSet exchangeObjectAtIndex:withObjectAtIndex:] : 1072 -> 1152
~ -[NSMutableOrderedSet insertObjects:count:atIndex:] : 1168 -> 1268
~ -[NSMutableOrderedSet minusOrderedSet:] : 620 -> 640
~ -[NSMutableOrderedSet minusSet:] : 540 -> 560
~ -[NSMutableOrderedSet removeObjectsInRange:] : 560 -> 600
~ -[NSMutableOrderedSet removeObject:inRange:] : 648 -> 688
~ -[NSMutableOrderedSet removeObjectsAtIndexes:] : 960 -> 1040
~ -[NSMutableOrderedSet removeObjectsInRange:inArray:range:] : 1180 -> 1280
~ -[NSMutableOrderedSet removeObjectsInRange:inArray:] : 916 -> 976
~ -[NSMutableOrderedSet removeObjectsInArray:range:] : 812 -> 872
~ -[NSMutableOrderedSet removeObjectsInArray:] : 532 -> 552
~ -[NSMutableOrderedSet removeObjectsInRange:inSet:] : 916 -> 976
~ -[NSMutableOrderedSet removeObjectsInSet:] : 532 -> 552
~ -[NSMutableOrderedSet removeObjectsAtIndexes:options:passingTest:] : 744 -> 804
~ -[NSMutableOrderedSet removeObjectsWithOptions:passingTest:] : 476 -> 496
~ -[NSMutableOrderedSet removeObjectsPassingTest:] : 364 -> 384
~ -[NSMutableOrderedSet replaceObject:inRange:] : 844 -> 904
~ -[NSMutableOrderedSet replaceObject:] : 440 -> 460
~ -[NSMutableOrderedSet replaceObjectsInRange:withObjects:count:] : 1296 -> 1396
~ -[NSMutableOrderedSet setArray:] : 396 -> 416
~ -[NSMutableOrderedSet setObject:atIndex:] : 844 -> 904
~ -[NSMutableOrderedSet setObject:] : 472 -> 492
~ -[NSMutableOrderedSet setOrderedSet:] : 448 -> 468
~ -[NSMutableOrderedSet setSet:] : 396 -> 416
~ -[NSMutableOrderedSet unionSet:] : 540 -> 560
~ -[NSMutableOrderedSet initWithObjects:count:] : 704 -> 764
~ -[__NSDictionaryI getObjects:andKeys:count:] : 516 -> 556
~ -[__NSDictionaryI countByEnumeratingWithState:objects:count:] : 588 -> 628
~ -[__NSSingleObjectSetI countByEnumeratingWithState:objects:count:] : 508 -> 548
~ -[__NSSingleObjectSetI enumerateObjectsWithOptions:usingBlock:] : 332 -> 352
~ -[__NSSingleObjectSetI getObjects:count:] : 464 -> 504
~ -[__NSPlaceholderSet initWithObjects:count:] : 896 -> 956
~ -[__NSPlaceholderSet initWithCapacity:] : 380 -> 400
~ -[__NSSingleEntryDictionaryI isEqualToDictionary:] : 448 -> 468
~ -[__NSSingleEntryDictionaryI getObjects:andKeys:count:] : 412 -> 452
~ -[__NSSingleEntryDictionaryI countByEnumeratingWithState:objects:count:] : 496 -> 536
~ -[__NSSingleEntryDictionaryI enumerateKeysAndObjectsWithOptions:usingBlock:] : 344 -> 364
~ -[NSConstantArray objectAtIndex:] : 484 -> 524
~ -[NSConstantArray getObjects:range:] : 1008 -> 1088
~ -[NSConstantArray objectAtIndexedSubscript:] : 484 -> 524
~ -[__NSOrderedSetReversed objectAtIndex:] : 504 -> 544
~ -[__NSSetI countByEnumeratingWithState:objects:count:] : 584 -> 624
~ -[__NSSetI getObjects:count:] : 568 -> 608
~ -[__NSSetI enumerateObjectsWithOptions:usingBlock:] : 576 -> 596
~ -[NSMutableDictionary addEntriesFromDictionary:] : 536 -> 556
~ -[NSMutableDictionary addObject:forKey:] : 560 -> 600
~ -[NSMutableDictionary addObjects:forKeys:count:] : 940 -> 1040
~ -[NSMutableDictionary addObjects:forKeys:] : 664 -> 704
~ -[NSMutableDictionary removeEntriesInDictionary:] : 576 -> 596
~ -[NSMutableDictionary removeEntriesWithOptions:passingTest:] : 668 -> 688
~ -[NSMutableDictionary removeEntriesPassingTest:] : 364 -> 384
~ -[NSMutableDictionary removeObjectsForKeys:] : 500 -> 520
~ -[NSMutableDictionary replaceObject:forKey:] : 560 -> 600
~ -[NSMutableDictionary replaceObjects:forKeys:count:] : 916 -> 1016
~ -[NSMutableDictionary replaceObjects:forKeys:] : 664 -> 704
~ -[NSMutableDictionary setEntriesFromDictionary:] : 536 -> 556
~ -[NSMutableDictionary setObjects:forKeys:count:] : 916 -> 1016
~ -[NSMutableDictionary setObjects:forKeys:] : 652 -> 692
~ -[NSMutableDictionary setDictionary:] : 544 -> 564
~ -[NSMutableDictionary __addObject:forKey:] : 560 -> 600
~ -[NSMutableDictionary __setObject:forKey:] : 536 -> 576
~ -[NSMutableDictionary initWithObjects:forKeys:count:] : 924 -> 1024
~ -[NSConstantDictionary getObjects:andKeys:count:] : 508 -> 548
~ -[NSConstantDictionary countByEnumeratingWithState:objects:count:] : 564 -> 604
~ -[NSConstantDictionary enumerateKeysAndObjectsWithOptions:usingBlock:] : 416 -> 436
~ -[NSConstantDictionary keysOfEntriesWithOptions:passingTest:] : 484 -> 504
~ -[NSArray componentsJoinedByString:] : 612 -> 632
~ -[NSArray containsObject:inRange:] : 652 -> 692
~ -[NSArray containsObjectIdenticalTo:inRange:] : 636 -> 676
~ -[NSArray countForObject:inRange:] : 596 -> 636
~ -[NSArray enumerateObjectsAtIndexes:options:usingBlock:] : 688 -> 748
~ -[NSArray enumerateObjectsWithOptions:usingBlock:] : 412 -> 432
~ -[NSArray enumerateObjectsUsingBlock:] : 364 -> 384
~ -[NSArray firstObjectCommonWithArray:] : 536 -> 556
~ -[NSArray getObjects:range:] : 908 -> 988
~ -[NSArray indexOfObject:inRange:] : 612 -> 652
~ -[NSArray indexOfObjectIdenticalTo:inRange:] : 576 -> 616
~ -[NSArray indexesOfObject:inRange:] : 648 -> 688
~ -[NSArray indexesOfObjectIdenticalTo:inRange:] : 648 -> 688
~ -[NSArray indexOfObject:inSortedRange:options:usingComparator:] : 1352 -> 1432
~ -[NSArray indexOfObjectAtIndexes:options:passingTest:] : 688 -> 748
~ -[NSArray indexOfObjectWithOptions:passingTest:] : 416 -> 436
~ -[NSArray indexOfObjectPassingTest:] : 364 -> 384
~ -[NSArray indexesOfObjectsAtIndexes:options:passingTest:] : 696 -> 756
~ -[NSArray indexesOfObjectsWithOptions:passingTest:] : 416 -> 436
~ -[NSArray indexesOfObjectsPassingTest:] : 364 -> 384
~ -[NSArray objectAtIndexes:options:passingTest:] : 720 -> 780
~ -[NSArray objectWithOptions:passingTest:] : 440 -> 460
~ -[NSArray objectPassingTest:] : 364 -> 384
~ -[NSArray objectsAtIndexes:options:passingTest:] : 656 -> 716
~ -[NSArray objectsWithOptions:passingTest:] : 380 -> 400
~ -[NSArray objectsPassingTest:] : 364 -> 384
~ +[NSArray newArrayWithObjects:count:] : 976 -> 1036
~ -[NSDictionary countByEnumeratingWithState:objects:count:] : 680 -> 720
~ -[NSDictionary enumerateKeysAndObjectsWithOptions:usingBlock:] : 392 -> 412
~ -[NSDictionary enumerateKeysAndObjectsUsingBlock:] : 364 -> 384
~ -[NSDictionary getObjects:andKeys:count:] : 604 -> 644
~ -[NSDictionary getObjects:andKeys:] : 472 -> 512
~ -[NSDictionary getKeys:] : 400 -> 420
~ -[NSDictionary getObjects:] : 400 -> 420
~ -[NSDictionary isEqualToDictionary:] : 616 -> 636
~ -[NSDictionary keyOfEntryWithOptions:passingTest:] : 464 -> 484
~ -[NSDictionary keyOfEntryPassingTest:] : 364 -> 384
~ -[NSDictionary keysOfEntriesWithOptions:passingTest:] : 520 -> 540
~ -[NSDictionary keysOfEntriesPassingTest:] : 364 -> 384
~ -[NSDictionary keysSortedByValueUsingComparator:] : 364 -> 384
~ +[NSDictionary newDictionaryWithObjects:forKeys:count:] : 1140 -> 1240
~ -[NSException initWithName:reason:userInfo:osLogPack:size:] : 348 -> 368
~ -[__NSArrayReversed objectAtIndex:] : 504 -> 544
~ -[__NSArrayReversed getObjects:range:] : 884 -> 964
~ -[NSMutableArray addObject:] : 380 -> 400
~ -[NSMutableArray addObjects:count:] : 776 -> 836
~ -[NSMutableArray addObjectsFromArray:range:] : 792 -> 852
~ -[NSMutableArray addObjectsFromOrderedSet:range:] : 792 -> 852
~ -[NSMutableArray addObjectsFromSet:] : 396 -> 416
~ -[NSMutableArray exchangeObjectAtIndex:withObjectAtIndex:] : 1052 -> 1132
~ -[NSMutableArray insertObjects:count:atIndex:] : 1148 -> 1248
~ -[NSMutableArray removeObjectsInRange:] : 560 -> 600
~ -[NSMutableArray removeObject:inRange:] : 644 -> 684
~ -[NSMutableArray removeObjectIdenticalTo:inRange:] : 628 -> 668
~ -[NSMutableArray removeObjectsAtIndexes:] : 960 -> 1040
~ -[NSMutableArray removeObjectsInRange:inArray:range:] : 1228 -> 1328
~ -[NSMutableArray removeObjectsInRange:inOrderedSet:range:] : 1176 -> 1276
~ -[NSMutableArray removeObjectsInRange:inSet:] : 804 -> 864
~ -[NSMutableArray removeObjectsAtIndexes:options:passingTest:] : 744 -> 804
~ -[NSMutableArray removeObjectsWithOptions:passingTest:] : 476 -> 496
~ -[NSMutableArray removeObjectsPassingTest:] : 304 -> 324
~ -[NSMutableArray replaceObject:inRange:] : 840 -> 900
~ -[NSMutableArray replaceObject:] : 460 -> 480
~ -[NSMutableArray setObject:atIndex:] : 844 -> 904
~ -[NSMutableArray sortUsingFunction:context:range:] : 744 -> 784
~ -[NSMutableArray initWithObjects:count:] : 704 -> 764
~ +[NSObject(NSObject) doesNotRecognizeSelector:] : 364 -> 384
~ -[NSObject(NSObject) doesNotRecognizeSelector:] : 364 -> 384
~ -[NSSet countByEnumeratingWithState:objects:count:] : 680 -> 720
~ -[NSSet enumerateObjectsUsingBlock:] : 364 -> 384
~ -[NSSet getObjects:count:] : 652 -> 692
~ -[NSSet getObjects:] : 544 -> 584
~ -[NSSet intersectsOrderedSet:] : 536 -> 556
~ -[NSSet isSubsetOfOrderedSet:] : 584 -> 604
~ -[NSSet objectPassingTest:] : 364 -> 384
~ -[NSSet objectsPassingTest:] : 364 -> 384
~ -[NSSet sortedArrayUsingComparator:] : 364 -> 384
~ +[NSSet newSetWithObjects:count:] : 972 -> 1032
~ -[__NSArrayI getObjects:range:] : 992 -> 1072
~ -[__NSArrayI countByEnumeratingWithState:objects:count:] : 488 -> 528
~ -[__NSArrayI_Transfer objectAtIndex:] : 480 -> 520
~ -[__NSArrayI_Transfer getObjects:range:] : 1008 -> 1088
~ -[__NSArrayI_Transfer countByEnumeratingWithState:objects:count:] : 504 -> 544
~ -[__NSArrayI_Transfer objectAtIndexedSubscript:] : 480 -> 520
~ -[__NSPlaceholderOrderedSet initWithCapacity:] : 380 -> 400
~ -[NSOrderedSet containsObject:inRange:] : 564 -> 604
~ -[NSOrderedSet countForObject:inRange:] : 564 -> 604
~ -[NSOrderedSet enumerateObjectsAtIndexes:options:usingBlock:] : 688 -> 748
~ -[NSOrderedSet enumerateObjectsWithOptions:usingBlock:] : 412 -> 432
~ -[NSOrderedSet enumerateObjectsUsingBlock:] : 364 -> 384
~ -[NSOrderedSet getObjects:range:] : 916 -> 996
~ -[NSOrderedSet indexOfObject:inRange:] : 568 -> 608
~ -[NSOrderedSet indexOfObject:inSortedRange:options:usingComparator:] : 1352 -> 1432
~ -[NSOrderedSet indexOfObjectAtIndexes:options:passingTest:] : 688 -> 748
~ -[NSOrderedSet indexOfObjectWithOptions:passingTest:] : 416 -> 436
~ -[NSOrderedSet indexOfObjectPassingTest:] : 364 -> 384
~ -[NSOrderedSet indexesOfObjectsAtIndexes:options:passingTest:] : 696 -> 756
~ -[NSOrderedSet indexesOfObjectsWithOptions:passingTest:] : 416 -> 436
~ -[NSOrderedSet indexesOfObjectsPassingTest:] : 364 -> 384
~ -[NSOrderedSet intersectsOrderedSet:] : 536 -> 556
~ -[NSOrderedSet intersectsSet:] : 536 -> 556
~ -[NSOrderedSet isSubsetOfOrderedSet:] : 552 -> 572
~ -[NSOrderedSet isSubsetOfSet:] : 552 -> 572
~ -[NSOrderedSet objectAtIndexes:options:passingTest:] : 720 -> 780
~ -[NSOrderedSet objectWithOptions:passingTest:] : 440 -> 460
~ -[NSOrderedSet objectPassingTest:] : 364 -> 384
~ -[NSOrderedSet objectsAtIndexes:options:passingTest:] : 676 -> 736
~ -[NSOrderedSet objectsWithOptions:passingTest:] : 400 -> 420
~ -[NSOrderedSet objectsPassingTest:] : 364 -> 384
~ +[NSOrderedSet newOrderedSetWithObjects:count:] : 820 -> 880
~ -[__NSSingleObjectArrayI objectAtIndex:] : 312 -> 332
~ -[__NSSingleObjectArrayI getObjects:range:] : 556 -> 596
~ -[__NSSingleObjectArrayI countByEnumeratingWithState:objects:count:] : 496 -> 536
~ -[__NSSingleObjectArrayI enumerateObjectsWithOptions:usingBlock:] : 336 -> 356
~ -[__NSSingleObjectArrayI isEqualToArray:] : 392 -> 412
~ -[NSSharedKeyDictionary getObjects:andKeys:count:] : 588 -> 628
~ -[__NSPlaceholderDictionary initWithObjects:forKeys:count:] : 1064 -> 1164
~ -[__NSPlaceholderDictionary initWithCapacity:] : 380 -> 400
~ -[__NSPlaceholderDictionary initWithContentsOfFile:] : 344 -> 364
~ -[__NSPlaceholderDictionary initWithContentsOfURL:] : 388 -> 408
~ -[__NSDictionaryM keysOfEntriesWithOptions:passingTest:] : 376 -> 396
~ -[__NSFrozenDictionaryM keysOfEntriesWithOptions:passingTest:] : 316 -> 336
~ _CFRunLoopAddCommonMode.cold.1 : 88 -> 80
~ _CFRunLoopGetNextTimerFireDate.cold.1 : 88 -> 80
~ _CFRunLoopIsWaiting.cold.1 : 88 -> 80
~ _CFRunLoopStop.cold.1 : 88 -> 80
~ _CFRunLoopContainsObserver.cold.1 : 88 -> 80
~ _CFRunLoopAddObserver.cold.1 : 88 -> 80
~ _CFRunLoopRemoveObserver.cold.1 : 88 -> 80
~ _CFRunLoopContainsTimer.cold.1 : 88 -> 80
~ _CFRunLoopAddTimer.cold.1 : 88 -> 80
~ _CFRunLoopRemoveTimer.cold.1 : 88 -> 80
~ ___CFRunLoopServiceMachPort.cold.1 : 164 -> 156
~ -[_CFXPreferences withSources:] : 116 -> 128
~ -[_CFXPreferences withNamedVolatileSources:] : 116 -> 128
~ -[CFPrefsSearchListSource setCloudEnabled:forKeyPrefix:] : 260 -> 276
~ -[CFPrefsSearchListSource setCloudEnabled:forKey:] : 224 -> 240
~ -[CFPrefsSearchListSource alreadylocked_useCloudForKey:] : 184 -> 180
~ -[CFPrefsSearchListSource alreadylocked_hasCloudValueForKey:] : 112 -> 108
~ -[_CFXPreferences withSearchLists:] : 128 -> 140
~ -[_CFPrefsSynchronizer disableTimer_alreadyLocked] : 64 -> 60
~ -[_CFPrefsSynchronizer noteDirtySource:] : 108 -> 116
~ -[_CFPrefsSynchronizer synchronizeForDaemonTermination] : 88 -> 96
~ -[_CFPrefsSynchronizer clear] : 80 -> 88
~ -[CFPrefsDaemon synchronousWithSourceCache:] : 140 -> 152
~ -[CFPrefsDaemon _setSource:isDead:] : 148 -> 144
~ -[CFPDSource _getUncanonicalizedPath:] : 124 -> 140
~ -[CFPDSource observingConnectionsLockedSync:] : 84 -> 92
~ -[CFPDSource stopNotifyingObserver:] : 88 -> 84
~ -[CFPDSource validateSandboxPermissionsForMessage:containerPath:accessType:] : 68 -> 72
~ -[CFPDSource handleAvoidCache] : 40 -> 36
~ -[CFPDSource handleNeverCache] : 40 -> 36
~ -[CFPDSource handleEUIDorEGIDMismatch] : 32 -> 28
~ -[CFPDSource handleSynchronous] : 32 -> 28
~ -[CFPDSource handleNoPlistFound] : 32 -> 28
~ -[CFPDSource attachSizeWarningsToReply:forByteCount:] : 80 -> 88
~ -[CFPrefsDaemon handleFlushSourceForDomainMessage:replyHandler:] : 240 -> 252
~ -[CFPrefsDaemon handleSimulateTimerSynchronizeForTesting] : 56 -> 60
~ ___56-[CFPrefsDaemon handleFlushManagedMessage:replyHandler:]_block_invoke_2 : 68 -> 64
~ -[CFPrefsDaemon updateShmemIndex:] : 64 -> 60
~ -[CFPrefsDaemon updateShmemForDomain:] : 200 -> 196
~ -[CFPrefsDaemon getShmemName:bufLen:] : 100 -> 96
~ -[CFPrefsDaemon updateEntireShmem] : 72 -> 68
~ -[_CFXPreferencesHandle _canUseCachedPersonaInfo] : 100 -> 96
~ -[_CFXPreferences _replaceDirectConnection:] : 144 -> 152
~ -[CFPrefsPlistSource _logLoudlyAboutSettingKey:] : 132 -> 128
~ -[CFPrefsPlistSource goVolatileAfterTryingToWriteKeys:values:count:] : 60 -> 56
~ -[CFPrefsPlistSource _shouldEnableDirectMode] : 104 -> 92
~ -[CFPrefsPlistSource goReadOnlyAfterTryingToWriteKeys:values:count:] : 60 -> 56
~ -[CFPrefsPlistSource attachAccessTokenToMessage:accessType:] : 204 -> 200

```
