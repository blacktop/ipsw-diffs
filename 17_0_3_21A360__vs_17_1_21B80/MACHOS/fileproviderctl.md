## fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

-1681.0.14.0.0
-  __TEXT.__text: 0x1ab9c
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_stubs: 0x3240
-  __TEXT.__objc_methlist: 0x608
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x724
-  __TEXT.__cstring: 0x48df
-  __TEXT.__ustring: 0xf86
-  __TEXT.__oslogstring: 0x2cf
-  __TEXT.__objc_methname: 0x2f3f
-  __TEXT.__objc_classname: 0x1df
-  __TEXT.__objc_methtype: 0x502
+1703.42.2.0.0
+  __TEXT.__text: 0x144f4
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_stubs: 0x2700
+  __TEXT.__objc_methlist: 0x3b0
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x5c4
+  __TEXT.__cstring: 0x3956
+  __TEXT.__ustring: 0x9a8
+  __TEXT.__oslogstring: 0x22b
+  __TEXT.__objc_methname: 0x25a3
+  __TEXT.__objc_classname: 0x1c0
+  __TEXT.__objc_methtype: 0x493
   __TEXT.__dlopen_cstrs: 0x94
-  __TEXT.__unwind_info: 0x6b0
-  __DATA_CONST.__auth_got: 0x5a0
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x19c0
-  __DATA_CONST.__cfstring: 0x3aa0
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_catlist: 0x20
+  __TEXT.__unwind_info: 0x568
+  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__const: 0x13e0
+  __DATA_CONST.__cfstring: 0x25a0
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2598
-  __DATA.__objc_selrefs: 0xde8
+  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x1d70
+  __DATA.__objc_selrefs: 0xb20
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1c8
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x98
-  __DATA.__objc_data: 0x2d0
+  __DATA.__objc_classrefs: 0x140
+  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0x734
-  __DATA.__bss: 0xc78
+  __DATA.__bss: 0xc60
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 441
-  Symbols:   318
-  CStrings:  1214
+  Functions: 341
+  Symbols:   278
+  CStrings:  942
 
Symbols:
+ _fpfs_enable_fts_thread_fchdir
- _FPActionDelete
- _FPActionReparent
- _FPActionTrash
- _FPFeatureFlagUserIgnoredItemsIsEnabled
- _FPItemDecorationTypeFolderStatus
- _NSClassFromString
- _NSCocoaErrorDomain
- _NSFileProviderSearchFilterContentTypeIdentifier
- _NSFileProviderSearchFilterFilename
- _NSFileProviderSearchFilterScopedToDirectory
- _NSFileProviderTrashContainerItemIdentifier
- _NSTemporaryDirectory
- _OBJC_CLASS_$_FPCopyOperation
- _OBJC_CLASS_$_FPCreateFolderOperation
- _OBJC_CLASS_$_FPDeleteOperation
- _OBJC_CLASS_$_FPDownloadOperation
- _OBJC_CLASS_$_FPEmptyAllTrashedItemsOperation
- _OBJC_CLASS_$_FPEvictOperation
- _OBJC_CLASS_$_FPIgnoreItemsOperation
- _OBJC_CLASS_$_FPMoveOperation
- _OBJC_CLASS_$_FPSetTagsOperation
- _OBJC_CLASS_$_FPTag
- _OBJC_CLASS_$_FPTrashOperation
- _OBJC_CLASS_$_FPUnignoreItemsOperation
- _OBJC_CLASS_$_NSFileProviderSearchQuery
- _OBJC_CLASS_$_NSObservableKeyPath
- _OBJC_EHTYPE_id
- _UTTypeItem
- ___NSDictionary0__struct
- __dispatch_source_type_signal
- _dispatch_assert_queue$V2
- _dispatch_block_create_with_qos_class
- _dispatch_resume
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _isatty
- _objc_copyWeak
- _objc_initWeak
- _objc_opt_respondsToSelector
- _rl_deprep_terminal
- _signal
CStrings:
+ "File Provider control utility.\n%s <command> <options>\n\nCommands:\n  listproviders                                                  - Show registered providers\n  thumbnail [<provider> <domain> <itemid>]|[<url>]               - dump thumbnail for an item\n  attributes <item> [--direct]                                   - get attributes for a url [from fpd]\n  dump [<domain|provider>]                                       - dump state of fileprovider's daemon\n      --limit-dump-size                                                 limit the number of items dumped\n  signal <provider> [<item id>]                                  - signal a provider on the given item (defaults to working set)\n  materialize <item>                                             - materialize the path on disk\n  evict <item>...                                                - make the paths on disk dataless\n      -n,--namespace                                                    attempt to evict directories\n  coordinate                                                     - perform a coordination on a given path\n      -R, --recursive <path>                                            perform a recursive read\n      -r, --read <path>                                                 perform a single item read\n      -w, --write <path>                                                perform a coordinated write\n      -d, --delete <path>                                               perform a coordinated delete\n      -t, --time <seconds>                                              hold coordination for this long (default: inf)\n      -e, --debug                                                       dump file coordination info\n  stabilize [<domain>...]                                        - wait for the domain to stabilize\n      -B, --barrier <item id>                                           apply a barrier on the specified item instead of a full stabilization\n  evaluate <item>                                                - evaluate finder actions and decorations on item\n  evaluate <action> [<item>] <target item>                       - evaluate finder interactions\n  domain <action> [<domainid>]                                   - modify domains properties\n  interactive-scheduling <domain>                                - interactive scheduling session\n  check | repair                                                 - run FPCK\n      -f                                                                perform a full dump (all items)\n      -a <path>                                                         perform check under path\n      -b <path>                                                         operate on an already created DB backup. If this is set you need to set -a to point to the domain root\n      -o <path>                                                         write output into file at path\n      -P                                                                no-pager output\n      -d                                                                dimisss low-importance invariants\n      -v                                                                print out files with broken invariants\n      -m [<providerDomainID>]                                           perform check on the d2d migration backup\n  obfuscate [<filename>/<path>...]                               - return the obfuscated form of the filename\n"
- "\x06\x13"
- "\t\t\"%@\" - "
- "\t%@:\n"
- "\t%@: (all clear)\n"
- "\t%@: no interaction\n"
- "\tevaluating \"%@\" -> "
- "\nExiting...\n"
- "\nInvalid identifier\n"
- "\nPlease enter an action (or ask for 'help' and 'quit')\n"
- "   %2lu:"
- " %@\n"
- " - [evict]able items"
- " - [fav]orited items"
- " - [materialized] <domain> items"
- " - [nonevict]able items"
- " - [pending] <domain> items"
- " - [recent] items"
- " - [search] <query> (try '(kMDItemDisplayName = \"keyword\"cdw)')"
- " - [server] <provider> <filename>"
- " - [share]d items"
- " - [trash]ed items"
- "%@ <itemID ...>\n"
- "%@ completed with error=%@\n"
- "%lu"
- "'.' is an alias for the current collection's identifier\n"
- "(failed)"
- ".."
- "<action> <itemID ...>\n"
- "@\"FPCTLTermDumper\""
- "@\"FPItem\""
- "@\"FPItemCollection\""
- "@\"NSDate\""
- "B16@?0@\"FPItemDecoration\"8"
- "B32@?0@\"FPItem\"8Q16^B24"
- "Debug"
- "Error fetching item: %@"
- "Error getting container item: %s\n"
- "Error missing arguments\n"
- "Exported to %@\n"
- "FPCTLCollectionDumper"
- "FPExtensionCollection"
- "FPMaterializedSetEnumerator"
- "FPPendingSetEnumerator"
- "File Provider control utility.\n%s <command> <options>\n\nCommands:\n  listproviders                                                  - Show registered providers\n  enumerate|ls <provider|collection>                             - enumerate a container\n      -v,--verbose                                                      verbose output\n      -i,--item <item id>                                               monitor a container other than root\n      -w,--workingset                                                   monitor the working set (equiv. to -i <working set identifier>)\n      -d,--sort-by-date                                                 sort by date instead of name\n      -t,--type <UTI>                                                   item type displayed in the enumeration (default: public.item)\n      -u,--thumbnail                                                    output thumbnails via 1337 escape code\n      -e,--no-cache                                                     don't use the cache on disk\n  thumbnail [<provider> <domain> <itemid>]|[<url>]               - dump thumbnail for an item\n  attributes <item> [--direct]                                   - get attributes for a url [from fpd]\n  dump [<domain|provider>]                                       - dump state of fileprovider's daemon\n      --limit-dump-size                                                 limit the number of items dumped\n  signal <provider> [<item id>]                                  - signal a provider on the given item (defaults to working set)\n  materialize <item>                                             - materialize the path on disk\n  evict <item>...                                                - make the paths on disk dataless\n      -n,--namespace                                                    attempt to evict directories\n  coordinate                                                     - perform a coordination on a given path\n      -R, --recursive <path>                                            perform a recursive read\n      -r, --read <path>                                                 perform a single item read\n      -w, --write <path>                                                perform a coordinated write\n      -d, --delete <path>                                               perform a coordinated delete\n      -t, --time <seconds>                                              hold coordination for this long (default: inf)\n      -e, --debug                                                       dump file coordination info\n  stabilize [<domain>...]                                        - wait for the domain to stabilize\n      -B, --barrier <item id>                                           apply a barrier on the specified item instead of a full stabilization\n  evaluate <item>                                                - evaluate finder actions and decorations on item\n  evaluate <action> [<item>] <target item>                       - evaluate finder interactions\n  domain <action> [<domainid>]                                   - modify domains properties\n  interactive-scheduling <domain>                                - interactive scheduling session\n  check | repair                                                 - run FPCK\n      -f                                                                perform a full dump (all items)\n      -a <path>                                                         perform check under path\n      -b <path>                                                         operate on an already created DB backup. If this is set you need to set -a to point to the domain root\n      -o <path>                                                         write output into file at path\n      -P                                                                no-pager output\n      -d                                                                dimisss low-importance invariants\n      -v                                                                print out files with broken invariants\n      -m [<providerDomainID>]                                           perform check on the d2d migration backup\n  obfuscate [<filename>/<path>...]                               - return the obfuscated form of the filename\n"
- "HIGH "
- "Item %@ not found"
- "Item is not a folder: %s\n"
- "LOW  "
- "MAX  "
- "MED  "
- "NO\n"
- "NONE "
- "No leftover validation items found\n"
- "Specialized Collections:"
- "Symbols used for events:\n"
- "Symbols used for items:\n"
- "T@\"FPItemCollection\",&,N,V_collection"
- "T@\"NSArray\",&,N,V_fileTypes"
- "T@\"NSArray\",&,N,V_sortDescriptors"
- "T@\"NSString\",&,N,V_collectionIdentifier"
- "T@\"NSString\",R,N,G_debugName"
- "T@?,N,V_completionHandler"
- "T@?,N,V_preDumpItem"
- "TB,N,V_showThumbnails"
- "TB,N,V_wantsDirectExtensionEnumeration"
- "Ti,N,V_verbose"
- "URL: %@\n"
- "URLByDeletingLastPathComponent"
- "Validation-"
- "ValidationFolder-"
- "YES\n"
- "You can use the name, identifier or index to refer to items\n"
- "[ERROR] %@ doesn't support searching by content type"
- "[ERROR] %@ doesn't support searching by file name"
- "[ERROR] %@ doesn't support searching scoped to an identifier"
- "_collection"
- "_collectionIdentifier"
- "_debugName"
- "_dumper"
- "_fileTypes"
- "_gatheringStartDate"
- "_item"
- "_preDumpItem"
- "_preflightActionsForActions:"
- "_showThumbnails"
- "_sortDescriptors"
- "_verbose"
- "_wantsDirectExtensionEnumeration"
- "actionCompletionBlock"
- "actions"
- "actions              show eligible actions\n"
- "actions <itemID ...>\n"
- "addObserverBlock:"
- "c"
- "cd"
- "cd                   enumerate a different directory\n"
- "cd <id>\n"
- "cleanup"
- "cleanup              remove all files that start with Validation-\n"
- "collection"
- "collection %@: received updates:\n"
- "collectionForFolderItem:"
- "collectionIdentifier"
- "continue             continue\n"
- "copy                 copy items\n"
- "copy itemID ... destination\n"
- "cp"
- "date"
- "debugName"
- "down"
- "download <item>\n"
- "download <item>      download an item\n"
- "dump                 dump all items\n"
- "dumpInteractions:forAction:sourceItems:destinationItem:"
- "dumpItem:"
- "dumpPrefix:item:"
- "dumpProgress:"
- "dumpThumbnailData:type:item:"
- "eligible actions for %lu items: %@\n"
- "eligible actions for dropping %lu items under \"%@\":\n"
- "eligibleActionsForDroppingItems:underItem:"
- "eligibleActionsForItems:"
- "empty-trash"
- "empty-trash          Empty the trashed items\n"
- "endLine"
- "enumerate"
- "enumeratedItemID"
- "error %s retrieving thumbnail for item %s\n"
- "error %s retrieving thumbnails\n"
- "export"
- "export <item> <path> export an item to a path\n"
- "export <item> [<path>]\n"
- "extensionCollection"
- "fav"
- "fetchParentsForItemID:recursively:completionHandler:"
- "fetchURLForItem:completionHandler:"
- "fileTypes"
- "finishObserving"
- "fp_categorize:"
- "fp_sortDescriptorByDisplayName"
- "fp_sortDescriptorByModifiedDateDescending"
- "gatherErrorsForInteractions:evaluationObjects:suppressionDelegate:"
- "gathering"
- "got thumbnail for %@\n"
- "hasMultipleProviderItems"
- "help                 show this help\n"
- "i"
- "i16@0:8"
- "i:t:vwdueT"
- "ignore"
- "ignore/unignore      update the ignore state for the item\n"
- "import"
- "import               import items\n"
- "import path1 path2 ...\n"
- "indexOfObjectPassingTest:"
- "info"
- "info                 fetch item info\n"
- "info <id>\n"
- "initWithDumper:"
- "initWithItems:"
- "initWithItems:destinationFolder:"
- "initWithItems:destinationURL:"
- "initWithItems:tagsLists:"
- "initWithLabel:color:"
- "initWithManager:"
- "initWithParentItem:folderName:"
- "initWithSearchScope:"
- "initWithURLs:destinationFolder:"
- "itemForIdentifier:"
- "itemForItemID:"
- "keyPathWithRootObject:path:"
- "localizedRecoveryOptions"
- "ls"
- "mainQueue"
- "materia"
- "mkdir"
- "mkdir                create folder\n"
- "mkdir <name>\n"
- "move"
- "move                 move items\n"
- "mv"
- "newCollectionForTag:"
- "newEvictableCollection"
- "newFavoritesCollection"
- "newNonAutoEvictableCollection"
- "newRecentsCollection"
- "newSearchCollection"
- "newSharedItemsCollection"
- "newTagCollection"
- "newTrashCollection"
- "no thumbnail for %@\n"
- "no-cache"
- "nonevict"
- "pend"
- "preDumpItem"
- "q"
- "recent"
- "remove               delete items\n"
- "reorderItemsWithSortDescriptors:"
- "resumeVendorEnumeration"
- "rootCollectionForProviderDomain:"
- "runCLI"
- "runCommand:"
- "scheduleOperation:"
- "scheduled %s\n"
- "search"
- "server"
- "setAllowedContentTypes:"
- "setCollection:"
- "setCollectionIdentifier:"
- "setFileTypes:"
- "setFilename:"
- "setPreDumpItem:"
- "setProviderDomainID:"
- "setSearchQuery:"
- "setShouldBounceOnCollision:"
- "setShouldPerformServerSearch:"
- "setShowThumbnails:"
- "setSortDescriptors:"
- "setTargetFilenamesByItem:"
- "setVerbose:"
- "setWantsDirectExtensionEnumeration:"
- "settags"
- "settags              set tags on item\n"
- "settags <itemID> [tag ...]\n"
- "settings"
- "setupCLI"
- "setupCollection:"
- "share"
- "showThumbnails"
- "sort"
- "sort <name|date>     change the sorting order\n"
- "sort-by-date"
- "startObserving"
- "stopObserving"
- "supportedSearchFilters"
- "suspendVendorEnumeration"
- "symbols"
- "symbols              print the meanings of the symbols\n"
- "tag"
- "tearDownCollection"
- "thu"
- "thumbnail fetch operation completed with unfetched thumbnails for items %s\n"
- "thumbnails           fetch thumbnails for listed items\n"
- "timeIntervalSinceDate:"
- "to copy to the current dir, use . for the destination\n"
- "trash"
- "trash                trash items\n"
- "trash <itemID ...>\n"
- "unignore"
- "updateDirectory:"
- "url"
- "url <item>           print URL of an item\n"
- "url <itemID>\n"
- "v16@?0@\"NSArray\"8"
- "v16@?0@8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@?0@\"FPItem\"8@\"FPCTLTermDumper\"16"
- "v24@?0@\"FPItemCollection\"8@\"NSError\"16"
- "v24@?0@\"NSString\"8^B16"
- "v32@?0@\"NSError\"8Q16^B24"
- "v48@0:8@16@24@32@40"
- "verbose"
- "wantsDirectExtensionEnumeration"
- "workingQueue"
- "workingset"

```
