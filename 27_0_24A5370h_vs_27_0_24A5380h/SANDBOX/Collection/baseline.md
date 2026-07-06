## baseline

> Group: ⬆️ Updated

```diff

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(profile-flag "disable-enforcement")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(extension-class "com.apple.mediaserverd.read")
+								(%entitlement-is-present "com.apple.private.applemediaservices")
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+							)
+							(require-all
+								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+								(require-any
+									(extension-class "com.apple.aned.read-only")
+									(extension-class "com.apple.app-sandbox.read")
+									(extension-class "com.apple.app-sandbox.read-write")
+									(extension-class "com.apple.mediaserverd.read")
+									(extension-class "com.apple.mediaserverd.read-write")
+									(extension-class "com.apple.nsurlsessiond.readonly")
+									(extension-class "com.apple.sharing.airdrop.readonly")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 					(require-all

 						(profile-flag "common-rules")
 					)
 					(require-all
-						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
 						(require-any
 							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 							(require-all
-								(profile-flag "common-rules")
+								(profile-flag "disable-enforcement")
 								(require-any
 									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 									(require-all

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(extension-class "com.apple.mediaserverd.read")
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-							)
-							(require-all
-								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.app-sandbox.read-write")
-									(extension-class "com.apple.mediaserverd.read")
-									(extension-class "com.apple.mediaserverd.read-write")
-									(extension-class "com.apple.nsurlsessiond.readonly")
-									(extension-class "com.apple.sharing.airdrop.readonly")
-								)
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 			)
 			(require-all
 				(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				(extension-class "com.apple.app-sandbox.read-write")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(extension-class "com.apple.aned.read-only")
-				(extension "com.apple.security.exception.files.home-relative-path.read-only")
+				(require-any
+					(extension "com.apple.security.exception.files.absolute-path.read-only")
+					(extension "com.apple.security.exception.files.home-relative-path.read-only")
+				)
 			)
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")

 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-				)
+				(extension "com.apple.security.exception.files.home-relative-path.read-only")
 			)
 		)
 	)

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(profile-flag "disable-enforcement")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(extension-class "com.apple.mediaserverd.read")
+								(%entitlement-is-present "com.apple.private.applemediaservices")
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+							)
+							(require-all
+								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+								(require-any
+									(extension-class "com.apple.aned.read-only")
+									(extension-class "com.apple.app-sandbox.read")
+									(extension-class "com.apple.app-sandbox.read-write")
+									(extension-class "com.apple.mediaserverd.read")
+									(extension-class "com.apple.mediaserverd.read-write")
+									(extension-class "com.apple.nsurlsessiond.readonly")
+									(extension-class "com.apple.sharing.airdrop.readonly")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 					(require-all

 						(profile-flag "common-rules")
 					)
 					(require-all
-						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
 						(require-any
 							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 							(require-all
-								(profile-flag "common-rules")
+								(profile-flag "disable-enforcement")
 								(require-any
 									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 									(require-all

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(extension-class "com.apple.mediaserverd.read")
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-							)
-							(require-all
-								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.app-sandbox.read-write")
-									(extension-class "com.apple.mediaserverd.read")
-									(extension-class "com.apple.mediaserverd.read-write")
-									(extension-class "com.apple.nsurlsessiond.readonly")
-									(extension-class "com.apple.sharing.airdrop.readonly")
-								)
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
+						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+						(require-any
+							(extension-class "com.apple.aned.read-only")
+							(extension-class "com.apple.app-sandbox.read")
+							(extension-class "com.apple.app-sandbox.read-write")
+							(extension-class "com.apple.mediaserverd.read")
+							(extension-class "com.apple.mediaserverd.read-write")
+							(extension-class "com.apple.nsurlsessiond.readonly")
+							(extension-class "com.apple.sharing.airdrop.readonly")
+						)
+					)
+					(require-all
+						(%entitlement-is-present "com.apple.security.system-groups")
 						(require-any
 							(require-all
 								(extension-class "com.apple.aned.read-only")

 							)
 							(require-all
 								(extension-class "com.apple.mediaserverd.read-write")
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+									)
+									(require-all
+										(extension-class "com.apple.mediaserverd.read-write")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+										)
+									)
+								)
 							)
 							(require-all
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")

 							)
 						)
 					)
-					(require-all
-						(%entitlement-is-present "com.apple.security.system-groups")
-						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-						(require-any
-							(extension-class "com.apple.aned.read-only")
-							(extension-class "com.apple.app-sandbox.read")
-							(extension-class "com.apple.app-sandbox.read-write")
-							(extension-class "com.apple.mediaserverd.read")
-							(extension-class "com.apple.mediaserverd.read-write")
-							(extension-class "com.apple.nsurlsessiond.readonly")
-							(extension-class "com.apple.sharing.airdrop.readonly")
-						)
-					)
 					(require-all
 						(extension-class "com.apple.mediaserverd.read")
 						(%entitlement-is-present "com.apple.private.applemediaservices")

 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
-				(%entitlement-is-present "com.apple.private.applemediaservices")
 				(require-any
-					(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-					(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+					(require-all
+						(%entitlement-is-present "com.apple.private.applemediaservices")
+						(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+					)
+					(require-all
+						(extension-class "com.apple.mediaserverd.read-write")
+						(%entitlement-is-present "com.apple.private.applemediaservices")
+						(require-any
+							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+						)
+					)
 				)
 			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(%entitlement-is-present "com.apple.private.applemediaservices")
-				(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(profile-flag "generic-sandbox-extension-support")
-		(require-any
-			(extension "com.apple.app-sandbox.read")
-			(extension "com.apple.app-sandbox.read-write")
-			(extension "com.apple.quicklook.readonly")
-			(extension "com.apple.security.exception.files.absolute-path.read-only")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-only")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(extension "com.apple.sharing.airdrop.readonly")
 		)
 	)
 )

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(profile-flag "generic-sandbox-extension-support")
+		(require-any
+			(extension "com.apple.app-sandbox.read")
+			(extension "com.apple.app-sandbox.read-write")
+			(extension "com.apple.quicklook.readonly")
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(extension "com.apple.sharing.airdrop.readonly")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(profile-flag "generic-sandbox-extension-support")
 		(require-any
 			(extension "com.apple.app-sandbox.read")

 		(require-any
 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
-				(extension "com.apple.app-sandbox.read-write")
+				(extension "com.apple.security.exception.files.home-relative-path.read-write")
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(extension "com.apple.app-sandbox.read-write")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
 				(require-any
 					(extension "com.apple.app-sandbox.read-write")
 					(extension "com.apple.security.exception.files.absolute-path.read-write")
 					(extension "com.apple.security.exception.files.home-relative-path.read-write")
 				)
 			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			)
 		)
 	)
 )

 					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.Argon")
 					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.FaceSupport")
 					(require-all
-						(system-attribute vendor-build)
-						(subpath "/usr/local")
+						(system-attribute internal-build)
+						(require-any
+							(subpath "/System/AppleInternal")
+							(subpath "/System/ExclaveCore")
+							(subpath "/usr/appleinternal")
+						)
 					)
 				)
 			)
 			(require-all
 				(system-attribute carrier-build)
-				(subpath "/usr/local")
+				(require-any
+					(subpath "/System/AppleInternal")
+					(subpath "/System/ExclaveCore")
+					(subpath "/usr/appleinternal")
+				)
 			)
 			(require-all
 				(system-attribute internal-build)
+				(require-any
+					(subpath "/System/AppleInternal")
+					(subpath "/System/ExclaveCore")
+					(subpath "/usr/appleinternal")
+				)
+			)
+			(require-all
+				(system-attribute vendor-build)
 				(require-any
 					(require-any
 						(subpath "/System/AppleInternal")

 					(subpath "/usr/local")
 				)
 			)
-			(require-all
-				(system-attribute vendor-build)
-				(subpath "/usr/local")
-			)
 			(subpath "/Developer")
 			(subpath "/System/Developer")
 			(subpath "/System/Library/Frameworks")

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "disable-enforcement")
 				(profile-flag "common-rules")
 				(require-any
 					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 							)
 						)
 					)
-					(require-all
-						(profile-flag "disable-enforcement")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
 				)
 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "common-rules")
 				(require-any
-					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 													)
 													(require-all
 														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
 														(require-any
 															(require-all
 																(%entitlement-is-bool-true "com.apple.coreduetd.people")

 															)
 														)
 													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
 													(require-any
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 													)
 													(require-all
 														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
 														(require-any
 															(require-all
 																(%entitlement-is-bool-true "com.apple.coreduetd.people")

 															)
 														)
 													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
 													(require-all
-														(vnode-type REGULAR-FILE)
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
 														(require-any
 															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
 															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
 														)
 													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
 													(require-any
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 )
 (allow file-read*
 	(require-all
-		(literal "/dev/aes_0")
+		(literal "/dev/dtracehelper")
 		(profile-flag "common-device-access")
 	)
 )

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "disable-enforcement")
 				(profile-flag "common-rules")
 				(require-any
 					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 							)
 						)
 					)
-					(require-all
-						(profile-flag "disable-enforcement")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
 				)
 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "common-rules")
 				(require-any
-					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 													)
 													(require-all
 														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
 														(require-any
 															(require-all
 																(%entitlement-is-bool-true "com.apple.coreduetd.people")

 															)
 														)
 													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
 													(require-any
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 													)
 													(require-all
 														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
 														(require-any
 															(require-all
 																(%entitlement-is-bool-true "com.apple.coreduetd.people")

 															)
 														)
 													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
 													(require-all
-														(vnode-type REGULAR-FILE)
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
 														(require-any
 															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
 															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
 														)
 													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
 													(require-any
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/preferences.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/CloudConfigurationSetAsideDetails.plist")
 		(profile-flag "common-apple-signed-executable-rules")
 		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow file-read*
 	(require-all
-		(literal "/dev/null")
-		(profile-flag "common-device-access")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(profile-flag "common-managed-configuration-read-rules")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}/Library/NanoTimeKit/FaceSupport")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.Argon")
+					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.FaceSupport")
+					(require-all
+						(system-attribute internal-build)
+						(require-any
+							(subpath "/System/AppleInternal")
+							(subpath "/System/ExclaveCore")
+							(subpath "/usr/appleinternal")
+						)
+					)
+				)
+			)
+			(require-all
+				(system-attribute carrier-build)
+				(require-any
+					(subpath "/System/AppleInternal")
+					(subpath "/System/ExclaveCore")
+					(subpath "/usr/appleinternal")
+				)
+			)
+			(require-all
+				(system-attribute internal-build)
+				(require-any
+					(subpath "/System/AppleInternal")
+					(subpath "/System/ExclaveCore")
+					(subpath "/usr/appleinternal")
+				)
+			)
+			(require-all
+				(system-attribute vendor-build)
+				(require-any
+					(require-any
+						(subpath "/System/AppleInternal")
+						(subpath "/System/ExclaveCore")
+						(subpath "/usr/appleinternal")
+					)
+					(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
+					(subpath "/AppleInternal")
+					(subpath "/usr/local")
+				)
+			)
+			(subpath "/Developer")
+			(subpath "/System/Developer")
+			(subpath "/System/Library/Frameworks")
+			(subpath "/System/Library/PrivateFrameworks")
+		)
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(profile-flag "common-debugging-rules")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}/Library/NanoTimeKit/FaceSupport")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.Argon")
-					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.FaceSupport")
-					(require-all
-						(system-attribute vendor-build)
-						(subpath "/usr/local")
-					)
-				)
-			)
-			(require-all
-				(system-attribute carrier-build)
-				(subpath "/usr/local")
-			)
-			(require-all
-				(system-attribute internal-build)
-				(require-any
-					(require-any
-						(subpath "/System/AppleInternal")
-						(subpath "/System/ExclaveCore")
-						(subpath "/usr/appleinternal")
-					)
-					(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
-					(subpath "/AppleInternal")
-					(subpath "/usr/local")
-				)
-			)
-			(require-all
-				(system-attribute vendor-build)
-				(subpath "/usr/local")
-			)
-			(subpath "/Developer")
-			(subpath "/System/Developer")
-			(subpath "/System/Library/Frameworks")
-			(subpath "/System/Library/PrivateFrameworks")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/dev/dtracehelper")
+		(literal "/dev/aes_0")
 		(profile-flag "common-device-access")
 	)
 )

 					(extension "com.apple.security.exception.files.absolute-path.bind")
 					(extension "com.apple.security.exception.files.absolute-path.connect")
 					(require-any
-						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-only}")
-						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-only}")
-						(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-only}")
+						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-write}")
+						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-write}")
+						(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-write}")
 					)
 				)
 			)

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(require-any
+			(literal "/dev/null")
+			(literal "/dev/zero")
+		)
+		(profile-flag "common-device-access")
+	)
+)
 (allow file-read*
 	(require-all
 		(profile-flag "common-device-access")

 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
+						(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
+						(extension "com.apple.sandbox.system-group")
+						(require-any
+							(%entitlement-is-present "com.apple.security.system-group-containers")
+							(%entitlement-is-present "com.apple.security.system-groups")
+						)
+					)
+					(require-all
+						(%entitlement-is-present "com.apple.security.system-groups")
 						(require-any
 							(require-all
 								(profile-flag "common-rules")

 							)
 						)
 					)
-					(require-all
-						(%entitlement-is-present "com.apple.security.system-groups")
-						(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
-						(extension "com.apple.sandbox.system-group")
-						(require-any
-							(%entitlement-is-present "com.apple.security.system-group-containers")
-							(%entitlement-is-present "com.apple.security.system-groups")
-						)
-					)
 					(require-all
 						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 						(extension "com.apple.sandbox.system-group")

 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(process-attribute is-apple-signed-executable)
-		(require-any
-			(literal "/System")
-			(literal "/private")
-			(literal "/private/preboot")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/dev/zero")
-		(profile-flag "common-device-access")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/CloudConfigurationSetAsideDetails.plist")
-		(profile-flag "common-apple-signed-executable-rules")
-		(process-attribute is-apple-signed-executable)
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "/usr/local/libexec")

 )
 (allow file-read*
 	(require-all
-		(profile-flag "common-managed-configuration-read-rules")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-		)
+		(literal "/private/var/preferences/SystemConfiguration/preferences.plist")
+		(profile-flag "common-apple-signed-executable-rules")
+		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow file-read*

 							)
 							(require-all
 								(vnode-type DIRECTORY)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-all
+								(vnode-type REGULAR-FILE)
 								(require-any
 									(require-all
 										(%entitlement-is-bool-true "com.apple.coreduetd.people")

 									)
 								)
 							)
-							(require-all
-								(vnode-type REGULAR-FILE)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
 							(require-any
 								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 					)
 					(require-all
 						(vnode-type DIRECTORY)
+						(require-any
+							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+						)
+					)
+					(require-all
+						(vnode-type REGULAR-FILE)
 						(require-any
 							(require-all
 								(%entitlement-is-bool-true "com.apple.coreduetd.people")

 							)
 						)
 					)
-					(require-all
-						(vnode-type REGULAR-FILE)
-						(require-any
-							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-						)
-					)
 					(require-any
 						(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 						(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "disable-enforcement")
 				(profile-flag "common-rules")
 				(require-any
 					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 							)
 						)
 					)
-					(require-all
-						(profile-flag "disable-enforcement")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
 				)
 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "common-rules")
 				(require-any
-					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 													)
 													(require-all
 														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
 														(require-any
 															(require-all
 																(%entitlement-is-bool-true "com.apple.coreduetd.people")

 															)
 														)
 													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
 													(require-any
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 											)
 											(require-all
 												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
 												(require-any
 													(require-all
 														(%entitlement-is-bool-true "com.apple.coreduetd.people")

 													)
 												)
 											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
 											(require-any
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 													)
 													(require-all
 														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
 														(require-any
 															(require-all
 																(%entitlement-is-bool-true "com.apple.coreduetd.people")

 															)
 														)
 													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
 													(require-all
-														(vnode-type REGULAR-FILE)
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
 														(require-any
 															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
 															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
 														)
 													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
 													(require-any
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 (allow file-read-metadata
 	(require-all
 		(profile-flag "common-debugging-rules")
-		(literal "${HOME}")
+		(literal "${HOME}/Library/Preferences")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(profile-flag "common-system-logging-rules")
-		(literal "/private/var/run/syslog")
+		(literal "/private/var/preferences/SystemConfiguration/preferences.plist")
+		(profile-flag "common-apple-signed-executable-rules")
+		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(literal "/dev/null")
+		(literal "/dev/aes_0")
 		(profile-flag "common-device-access")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/dev/zero")
-		(profile-flag "common-device-access")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(literal "/dev/aes_0")
-		(profile-flag "common-device-access")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/preferences.plist")
 		(profile-flag "common-apple-signed-executable-rules")
 		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "${HOME}")
+			(literal "${HOME}/Library/Preferences")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(require-any
+			(literal "/dev/null")
+			(literal "/dev/zero")
+		)
+		(profile-flag "common-device-access")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(profile-flag "common-apple-signed-executable-rules")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
+			(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/CloudConfigurationDetails.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.system-container")
+		(extension "com.apple.sandbox.system-container")
+		(require-any
+			(require-all
+				(literal "/private/var/containers/Data/System/[^/]+/.com.apple.*")
+				(profile-flag "common-rules")
+			)
+			(require-all
+				(profile-flag "common-rules")
+				(require-any
+					(require-all
+						(subpath "/private/var/containers/Data/System")
+						(regex #"^/private/var/containers/Data/System/[^/]+(/|$)")
+					)
+					(subpath "/private/var/containers/Data/System/[^/]+")
+				)
+			)
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(profile-flag "common-managed-configuration-read-rules")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/CloudConfigurationSetAsideDetails.plist")
+			(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/CloudConfigurationSetAsideDetails.plist")
+		)
+		(profile-flag "common-apple-signed-executable-rules")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(profile-flag "common-exception-entitlement-rules")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/usr/libexec")
+		(profile-flag "common-apple-signed-executable-rules")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(profile-flag "common-rules")
+		(require-any
+			(extension "com.apple.sandbox.executable")
+			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
+			(literal "/private/etc/fstab")
+			(literal "/private/etc/hosts")
+			(literal "/private/etc/passwd")
+			(literal "/private/etc/services")
+			(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
+			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
+			(literal "/private/var/db/eligibilityd/eligibility.plist")
+			(require-all
+				(literal "/private/etc/master.passwd")
+				(uid 0)
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.bin")
+				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.plist")
+			)
+			(require-any
+				(literal "/private/etc/group")
+				(literal "/private/etc/protocols")
+			)
+			(subpath "/Library/RegionFeatures")
+			(subpath "/System/Library")
+			(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+			(subpath "/private/var/db/datadetectors/sys")
+			(subpath "/private/var/db/timezone")
+			(subpath "/private/var/preferences/Logging")
+			(subpath "/usr/lib")
+			(subpath "/usr/share")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/usr/local/libexec")
+		(system-attribute internal-build)
+		(profile-flag "common-apple-signed-executable-rules")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(profile-flag "generic-sandbox-extension-support")
+		(require-any
+			(extension "com.apple.app-sandbox.read")
+			(extension "com.apple.app-sandbox.read-write")
+			(extension "com.apple.quicklook.readonly")
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(extension "com.apple.sharing.airdrop.readonly")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.sandbox.system-group")
+		(require-any
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "disable-enforcement")
+				(profile-flag "common-rules")
+				(require-any
+					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+						(require-any
+							(require-all
+								(%entitlement-is-present "com.apple.private.applemediaservices")
+								(require-any
+									(require-all
+										(%entitlement-is-bool-true "com.apple.coreduetd.people")
+										(require-any
+											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+											(require-any
+												(literal "${HOME}/Library/CoreDuet/People")
+												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+											)
+										)
+									)
+									(require-all
+										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-any
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+									)
+								)
+							)
+							(require-all
+								(extension "com.apple.logd.read-only")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-any
+										(subpath "/private/var/db/diagnostics")
+										(subpath "/private/var/db/uuidtext")
+									)
+									(require-any
+										(subpath "/private/var/db/timesync")
+										(subpath "/private/var/userdata/diagnostics")
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+						(require-any
+							(require-all
+								(%entitlement-is-present "com.apple.private.applemediaservices")
+								(require-any
+									(require-all
+										(%entitlement-is-bool-true "com.apple.coreduetd.people")
+										(require-any
+											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+											(require-any
+												(literal "${HOME}/Library/CoreDuet/People")
+												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+											)
+										)
+									)
+									(require-all
+										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-any
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+									)
+								)
+							)
+							(require-all
+								(extension "com.apple.logd.read-only")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-any
+										(subpath "/private/var/db/diagnostics")
+										(subpath "/private/var/db/uuidtext")
+									)
+									(require-any
+										(subpath "/private/var/db/timesync")
+										(subpath "/private/var/userdata/diagnostics")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
+								(require-any
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(%entitlement-is-bool-true "com.apple.coreduetd.people")
+												(require-any
+													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+													(require-any
+														(literal "${HOME}/Library/CoreDuet/People")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+													)
+												)
+											)
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(extension "com.apple.logd.read-only")
+										(require-any
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(%entitlement-is-bool-true "com.apple.coreduetd.people")
+														(require-any
+															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+															(require-any
+																(literal "${HOME}/Library/CoreDuet/People")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+															)
+														)
+													)
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(require-all
+																(%entitlement-is-bool-true "com.apple.coreduetd.people")
+																(require-any
+																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
+																	(require-any
+																		(literal "${HOME}/Library/CoreDuet/People")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
+																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
+																	)
+																)
+															)
+															(require-any
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+															)
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+											(require-any
+												(subpath "/private/var/db/diagnostics")
+												(subpath "/private/var/db/uuidtext")
+											)
+											(require-any
+												(subpath "/private/var/db/timesync")
+												(subpath "/private/var/userdata/diagnostics")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
 	)
 )
 (allow file-read-metadata

 				(%entitlement-is-bool-true "com.apple.security.system-container")
 				(require-any
 					(require-all
-						(%entitlement-is-present "com.apple.security.system-groups")
+						(%entitlement-is-present "com.apple.security.system-group-containers")
 						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 						(extension "com.apple.sandbox.system-group")
 					)

 						(require-any
 							(extension "com.apple.sandbox.system-container")
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(extension "com.apple.sandbox.system-group")
 							)

 )
 (allow file-read-metadata
 	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(require-any
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-		)
+		(profile-flag "common-system-logging-rules")
+		(literal "/private/var/run/syslog")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(profile-flag "generic-sandbox-extension-support")
+		(process-attribute is-apple-signed-executable)
 		(require-any
-			(extension "com.apple.app-sandbox.read")
-			(extension "com.apple.app-sandbox.read-write")
-			(extension "com.apple.quicklook.readonly")
-			(extension "com.apple.security.exception.files.absolute-path.read-only")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-only")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(extension "com.apple.sharing.airdrop.readonly")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(profile-flag "common-rules")
-		(require-any
-			(extension "com.apple.sandbox.executable")
-			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
-			(literal "/private/etc/fstab")
-			(literal "/private/etc/hosts")
-			(literal "/private/etc/passwd")
-			(literal "/private/etc/services")
-			(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
-			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
-			(literal "/private/var/db/eligibilityd/eligibility.plist")
-			(require-all
-				(literal "/private/etc/master.passwd")
-				(uid 0)
-			)
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.bin")
-				(literal "${FRONT_USER_HOME}/Library/Application Support/com.apple.palette.green.plist")
-			)
-			(require-any
-				(literal "/private/etc/group")
-				(literal "/private/etc/protocols")
-			)
-			(subpath "/Library/RegionFeatures")
-			(subpath "/System/Library")
-			(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-			(subpath "/private/var/db/datadetectors/sys")
-			(subpath "/private/var/db/timezone")
-			(subpath "/private/var/preferences/Logging")
-			(subpath "/usr/lib")
-			(subpath "/usr/share")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.system-container")
-		(extension "com.apple.sandbox.system-container")
-		(require-any
-			(require-all
-				(literal "/private/var/containers/Data/System/[^/]+/.com.apple.*")
-				(profile-flag "common-rules")
-			)
-			(require-all
-				(profile-flag "common-rules")
-				(require-any
-					(require-all
-						(subpath "/private/var/containers/Data/System")
-						(regex #"^/private/var/containers/Data/System/[^/]+(/|$)")
-					)
-					(subpath "/private/var/containers/Data/System/[^/]+")
-				)
-			)
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.sandbox.system-group")
-		(require-any
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-group-containers")
-				(profile-flag "common-rules")
-				(require-any
-					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(profile-flag "disable-enforcement")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "common-rules")
-				(require-any
-					(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-						(require-any
-							(require-all
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(%entitlement-is-bool-true "com.apple.coreduetd.people")
-										(require-any
-											(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-											(require-any
-												(literal "${HOME}/Library/CoreDuet/People")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-												(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-											)
-										)
-									)
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(extension "com.apple.logd.read-only")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-any
-										(subpath "/private/var/db/diagnostics")
-										(subpath "/private/var/db/uuidtext")
-									)
-									(require-any
-										(subpath "/private/var/db/timesync")
-										(subpath "/private/var/userdata/diagnostics")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(profile-flag "disable-enforcement")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.logging.diagnostic")
-								(require-any
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(%entitlement-is-bool-true "com.apple.coreduetd.people")
-												(require-any
-													(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-													(require-any
-														(literal "${HOME}/Library/CoreDuet/People")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-														(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-													)
-												)
-											)
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(extension "com.apple.logd.read-only")
-										(require-any
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(%entitlement-is-bool-true "com.apple.coreduetd.people")
-														(require-any
-															(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-															(require-any
-																(literal "${HOME}/Library/CoreDuet/People")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-															)
-														)
-													)
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(require-all
-																(%entitlement-is-bool-true "com.apple.coreduetd.people")
-																(require-any
-																	(literal "${HOME}/Library/CoreDuet/People/interactionC.db-shm")
-																	(require-any
-																		(literal "${HOME}/Library/CoreDuet/People")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-journal")
-																		(literal "${HOME}/Library/CoreDuet/People/interactionC.db-wal")
-																	)
-																)
-															)
-															(require-any
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-																(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-															)
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-											(require-any
-												(subpath "/private/var/db/diagnostics")
-												(subpath "/private/var/db/uuidtext")
-											)
-											(require-any
-												(subpath "/private/var/db/timesync")
-												(subpath "/private/var/userdata/diagnostics")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
+			(literal "/System")
+			(literal "/private")
+			(literal "/private/preboot")
 		)
 	)
 )

 					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.Argon")
 					(%entitlement-is-bool-true "com.apple.private.security.storage.NanoTimeKit.FaceSupport")
 					(require-all
-						(system-attribute vendor-build)
-						(subpath "/usr/local")
+						(system-attribute internal-build)
+						(require-any
+							(subpath "/System/AppleInternal")
+							(subpath "/System/ExclaveCore")
+							(subpath "/usr/appleinternal")
+						)
 					)
 				)
 			)
 			(require-all
 				(system-attribute carrier-build)
-				(subpath "/usr/local")
+				(require-any
+					(subpath "/System/AppleInternal")
+					(subpath "/System/ExclaveCore")
+					(subpath "/usr/appleinternal")
+				)
 			)
 			(require-all
 				(system-attribute internal-build)
+				(require-any
+					(subpath "/System/AppleInternal")
+					(subpath "/System/ExclaveCore")
+					(subpath "/usr/appleinternal")
+				)
+			)
+			(require-all
+				(system-attribute vendor-build)
 				(require-any
 					(require-any
 						(subpath "/System/AppleInternal")

 					(subpath "/usr/local")
 				)
 			)
-			(require-all
-				(system-attribute vendor-build)
-				(subpath "/usr/local")
-			)
 			(subpath "/Developer")
 			(subpath "/System/Developer")
 			(subpath "/System/Library/Frameworks")

 					(extension "com.apple.security.exception.files.absolute-path.bind")
 					(extension "com.apple.security.exception.files.absolute-path.connect")
 					(require-any
-						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-only}")
-						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-only}")
-						(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-only}")
+						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-write}")
+						(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.exception.nano-preference.read-write}")
+						(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.exception.nano-paired-storage.subpath.read-write}")
 					)
 				)
 			)

 )
 (allow file-read-metadata
 	(require-all
-		(profile-flag "common-apple-signed-executable-rules")
-		(process-attribute is-apple-signed-executable)
+		(profile-flag "common-device-access")
 		(require-any
-			(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
-			(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/CloudConfigurationDetails.plist")
-			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
+			(literal "/dev/random")
+			(literal "/dev/urandom")
 		)
 	)
 )

 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
+						(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
+						(extension "com.apple.sandbox.system-group")
+						(require-any
+							(%entitlement-is-present "com.apple.security.system-group-containers")
+							(%entitlement-is-present "com.apple.security.system-groups")
+						)
+					)
+					(require-all
+						(%entitlement-is-present "com.apple.security.system-groups")
 						(require-any
 							(require-all
 								(profile-flag "common-rules")

 							)
 						)
 					)
-					(require-all
-						(%entitlement-is-present "com.apple.security.system-groups")
-						(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
-						(extension "com.apple.sandbox.system-group")
-						(require-any
-							(%entitlement-is-present "com.apple.security.system-group-containers")
-							(%entitlement-is-present "com.apple.security.system-groups")
-						)
-					)
 					(require-all
 						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 						(extension "com.apple.sandbox.system-group")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(profile-flag "common-apple-signed-executable-rules")
-		(process-attribute is-apple-signed-executable)
-		(require-any
-			(literal "${HOME}")
-			(literal "${HOME}/Library/Preferences")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(profile-flag "common-rules")

 							)
 							(require-all
 								(vnode-type DIRECTORY)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-all
+								(vnode-type REGULAR-FILE)
 								(require-any
 									(require-all
 										(%entitlement-is-bool-true "com.apple.coreduetd.people")

 									)
 								)
 							)
-							(require-all
-								(vnode-type REGULAR-FILE)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
 							(require-any
 								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 									)
 									(require-all
 										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
 										(require-any
 											(require-all
 												(%entitlement-is-bool-true "com.apple.coreduetd.people")

 											)
 										)
 									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
 									(require-any
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 					)
 					(require-all
 						(vnode-type DIRECTORY)
+						(require-any
+							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+						)
+					)
+					(require-all
+						(vnode-type REGULAR-FILE)
 						(require-any
 							(require-all
 								(%entitlement-is-bool-true "com.apple.coreduetd.people")

 							)
 						)
 					)
-					(require-all
-						(vnode-type REGULAR-FILE)
-						(require-any
-							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-							(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-						)
-					)
 					(require-any
 						(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
 						(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(process-attribute is-apple-signed-executable)
-		(require-any
-			(literal "/System")
-			(literal "/private")
-			(literal "/private/preboot")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(profile-flag "common-device-access")
-		(require-any
-			(literal "/dev/random")
-			(literal "/dev/urandom")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "/usr/libexec")
-		(profile-flag "common-apple-signed-executable-rules")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "/usr/local/libexec")
-		(system-attribute internal-build)
-		(profile-flag "common-apple-signed-executable-rules")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/CloudConfigurationSetAsideDetails.plist")
-			(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/CloudConfigurationSetAsideDetails.plist")
-		)
-		(profile-flag "common-apple-signed-executable-rules")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(profile-flag "common-managed-configuration-read-rules")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-any
 		(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")

 			)
 			(require-all
 				(system-attribute internal-build)
+				(subpath "/System/ExclaveCore")
+			)
+			(require-all
+				(system-attribute vendor-build)
 				(require-any
 					(subpath "/System/ExclaveCore")
 					(subpath "/System/Library/PrivateFrameworks")
 				)
 			)
-			(require-all
-				(system-attribute vendor-build)
-				(subpath "/System/ExclaveCore")
-			)
 			(subpath "/System/Library/Frameworks")
 			(subpath "/System/Library/PrivateFrameworks")
 		)

 								(require-any
 									(require-all
 										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-groups")
 										(require-any
 											(require-all
 												(subpath "/")

 											(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 										)
 									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-									)
 									(require-all
 										(subpath "/")
 										(process-attribute is-apple-signed-executable)

 										(require-any
 											(require-all
 												(%entitlement-is-present "com.apple.security.system-group-containers")
+												(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+											)
+											(require-all
+												(%entitlement-is-present "com.apple.security.system-groups")
 												(require-any
 													(require-all
 														(subpath "/")

 													(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 												)
 											)
-											(require-all
-												(%entitlement-is-present "com.apple.security.system-groups")
-												(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-											)
 											(require-all
 												(subpath "/")
 												(process-attribute is-apple-signed-executable)

 						(require-any
 							(require-all
 								(%entitlement-is-present "com.apple.security.system-group-containers")
+								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+							)
+							(require-all
+								(%entitlement-is-present "com.apple.security.system-groups")
 								(require-any
 									(require-all
 										(subpath "/")

 									(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								)
 							)
-							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
-								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-							)
 							(require-all
 								(subpath "/")
 								(process-attribute is-apple-signed-executable)

 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
+						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+					)
+					(require-all
+						(%entitlement-is-present "com.apple.security.system-groups")
 						(require-any
 							(require-all
 								(subpath "/")

 							(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 						)
 					)
-					(require-all
-						(%entitlement-is-present "com.apple.security.system-groups")
-						(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-					)
 					(require-all
 						(subpath "/")
 						(process-attribute is-apple-signed-executable)

 		)
 	)
 )
-(allow file-test-existence
-	(require-all
-		(literal "/private")
-		(process-attribute is-apple-signed-executable)
-	)
-)
 (allow file-test-existence
 	(require-all
 		(literal "/System")

 		(process-attribute is-apple-signed-executable)
 	)
 )
+(allow file-test-existence
+	(require-all
+		(literal "/private")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-test-existence
 	(require-any
 		(subpath "/")

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+				(require-any
+					(extension "com.apple.sandbox.system-group")
+					(require-all
+						(%entitlement-is-present "com.apple.private.applemediaservices")
+						(require-any
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-all
+								(vnode-type REGULAR-FILE)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-any
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.private.applemediaservices")

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-				(require-any
-					(extension "com.apple.sandbox.system-group")
-					(require-all
-						(%entitlement-is-present "com.apple.private.applemediaservices")
-						(require-any
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-all
-								(vnode-type REGULAR-FILE)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-any
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+				(require-any
+					(extension "com.apple.sandbox.system-group")
+					(require-all
+						(%entitlement-is-present "com.apple.private.applemediaservices")
+						(require-any
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-all
+								(vnode-type REGULAR-FILE)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-any
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.private.applemediaservices")

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-				(require-any
-					(extension "com.apple.sandbox.system-group")
-					(require-all
-						(%entitlement-is-present "com.apple.private.applemediaservices")
-						(require-any
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-all
-								(vnode-type REGULAR-FILE)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-any
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 )
 (deny file-write-create)
 
-(allow file-write-data
-	(with report)
-	(require-all
-		(literal "/dev/urandom")
-		(profile-flag "disable-enforcement")
-		(profile-flag "common-device-access")
-	)
-)
 (allow file-write-data
 	(with report)
 	(profile-flag "disable-enforcement")

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(profile-flag "disable-enforcement")
+						(require-any
+							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+								(%entitlement-is-present "com.apple.private.applemediaservices")
+								(require-any
+									(require-all
+										(vnode-type DIRECTORY)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-all
+										(vnode-type REGULAR-FILE)
+										(require-any
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+										)
+									)
+									(require-any
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+									)
+								)
+							)
+							(require-all
+								(%entitlement-is-present "com.apple.security.system-group-containers")
+								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+								(require-any
+									(extension "com.apple.sandbox.system-group")
+									(require-all
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 					(require-all

 						(profile-flag "common-rules")
 					)
 					(require-all
-						(profile-flag "disable-enforcement")
+						(profile-flag "common-rules")
 						(require-any
 							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 							(require-all
-								(profile-flag "common-rules")
+								(profile-flag "disable-enforcement")
 								(require-any
 									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 									(require-all

 										)
 									)
 									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
+										(%entitlement-is-present "com.apple.security.system-group-containers")
 										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 										(require-any
 											(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
-						(require-any
-							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-								(%entitlement-is-present "com.apple.private.applemediaservices")
-								(require-any
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-all
-										(vnode-type REGULAR-FILE)
-										(require-any
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-											(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-										)
-									)
-									(require-any
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-										(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-									)
-								)
-							)
-							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
-								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-								(require-any
-									(extension "com.apple.sandbox.system-group")
-									(require-all
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 	(with report)
 	(require-all
 		(literal "/dev/random")
-		(require-any
-			(profile-flag "common-device-access")
-			(require-all
-				(profile-flag "disable-enforcement")
-				(profile-flag "common-device-access")
-			)
-		)
+		(profile-flag "common-device-access")
+		(profile-flag "disable-enforcement")
+	)
+)
+(allow file-write-data
+	(with report)
+	(require-all
+		(literal "/dev/urandom")
+		(profile-flag "common-device-access")
+		(profile-flag "disable-enforcement")
 	)
 )
 (allow file-write-data

 		(profile-flag "common-device-access")
 		(require-any
 			(literal "/dev/dtracehelper")
-			(literal "/dev/null")
-			(literal "/dev/zero")
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+				(require-any
+					(extension "com.apple.sandbox.system-group")
+					(require-all
+						(%entitlement-is-present "com.apple.private.applemediaservices")
+						(require-any
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-all
+								(vnode-type REGULAR-FILE)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-any
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.private.applemediaservices")

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-				(require-any
-					(extension "com.apple.sandbox.system-group")
-					(require-all
-						(%entitlement-is-present "com.apple.private.applemediaservices")
-						(require-any
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-all
-								(vnode-type REGULAR-FILE)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-any
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 	(with no-report)
 	(require-all
 		(literal "/dev/random")
-		(require-any
-			(profile-flag "common-device-access")
-			(require-all
-				(profile-flag "disable-enforcement")
-				(profile-flag "common-device-access")
-			)
-		)
+		(profile-flag "common-device-access")
+		(profile-flag "disable-enforcement")
+	)
+)
+(deny file-write-data
+	(with no-report)
+	(require-all
+		(literal "/dev/urandom")
+		(profile-flag "common-device-access")
+		(profile-flag "disable-enforcement")
 	)
 )
 (deny file-write-data)

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(profile-flag "common-rules")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-						(profile-flag "common-rules")
-					)
 					(require-all
 						(profile-flag "disable-enforcement")
-						(require-any
-							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-							(require-all
-								(profile-flag "common-rules")
-								(require-any
-									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-										(%entitlement-is-present "com.apple.private.applemediaservices")
-										(require-any
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-all
-												(vnode-type REGULAR-FILE)
-												(require-any
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-												)
-											)
-											(require-any
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-											)
-										)
-									)
-									(require-all
-										(%entitlement-is-present "com.apple.security.system-groups")
-										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-										(require-any
-											(extension "com.apple.sandbox.system-group")
-											(require-all
-												(%entitlement-is-present "com.apple.private.applemediaservices")
-												(require-any
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-all
-														(vnode-type REGULAR-FILE)
-														(require-any
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-														)
-													)
-													(require-any
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(profile-flag "disable-enforcement")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-					(require-all
-						(profile-flag "common-rules")
 						(require-any
 							(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
 							(require-all

 								)
 							)
 							(require-all
-								(%entitlement-is-present "com.apple.security.system-groups")
+								(%entitlement-is-present "com.apple.security.system-group-containers")
 								(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
 								(require-any
 									(extension "com.apple.sandbox.system-group")

 					)
 				)
 			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(require-all
+						(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+						(profile-flag "common-rules")
+					)
+					(require-all
+						(profile-flag "common-rules")
+						(require-any
+							(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+							(require-all
+								(profile-flag "disable-enforcement")
+								(require-any
+									(literal "/private/var/containers/Shared/SystemGroup/[^/]+/.com.apple.*")
+									(require-all
+										(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+										(%entitlement-is-present "com.apple.private.applemediaservices")
+										(require-any
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-all
+												(vnode-type REGULAR-FILE)
+												(require-any
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+													(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+												)
+											)
+											(require-any
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+												(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+											)
+										)
+									)
+									(require-all
+										(%entitlement-is-present "com.apple.security.system-group-containers")
+										(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+										(require-any
+											(extension "com.apple.sandbox.system-group")
+											(require-all
+												(%entitlement-is-present "com.apple.private.applemediaservices")
+												(require-any
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-all
+														(vnode-type REGULAR-FILE)
+														(require-any
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+															(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+														)
+													)
+													(require-any
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+														(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
 		)
 	)
 )

 			)
 			(require-all
 				(%entitlement-is-present "com.apple.security.system-group-containers")
+				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
+				(require-any
+					(extension "com.apple.sandbox.system-group")
+					(require-all
+						(%entitlement-is-present "com.apple.private.applemediaservices")
+						(require-any
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-all
+								(vnode-type REGULAR-FILE)
+								(require-any
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
+									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
+								)
+							)
+							(require-any
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
+								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(%entitlement-is-present "com.apple.security.system-groups")
 				(require-any
 					(require-all
 						(%entitlement-is-present "com.apple.private.applemediaservices")

 					)
 				)
 			)
-			(require-all
-				(%entitlement-is-present "com.apple.security.system-groups")
-				(subpath "/private/var/containers/Shared/SystemGroup/[^/]+")
-				(require-any
-					(extension "com.apple.sandbox.system-group")
-					(require-all
-						(%entitlement-is-present "com.apple.private.applemediaservices")
-						(require-any
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-all
-								(vnode-type REGULAR-FILE)
-								(require-any
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServices")
-									(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleMediaServicesKit")
-								)
-							)
-							(require-any
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServices")
-								(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.AppleMediaServicesKit")
-							)
-						)
-					)
-				)
-			)
 		)
 	)
 )

 )
 (allow sysctl-read
 	(require-all
-		(sysctl-name "hw.pagesize_compat")
+		(sysctl-name "vm.footprint_suspend")
 		(profile-flag "common-exception-entitlement-rules")
-		(extension "com.apple.security.exception.sysctl.read-write")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "kern.osrelease")
-		(profile-flag "common-exception-entitlement-rules")
-		(extension "com.apple.security.exception.sysctl.read-write")
+		(extension "com.apple.security.exception.sysctl.read-only")
 	)
 )
 (allow sysctl-read

 		)
 	)
 )
+(allow sysctl-read
+	(require-all
+		(sysctl-name "hw.pagesize_compat")
+		(profile-flag "common-exception-entitlement-rules")
+		(extension "com.apple.security.exception.sysctl.read-only")
+	)
+)
+(allow sysctl-read
+	(require-all
+		(sysctl-name "vm.task_no_footprint_for_debug")
+		(profile-flag "common-exception-entitlement-rules")
+		(extension "com.apple.security.exception.sysctl.read-only")
+	)
+)
+(allow sysctl-read
+	(require-all
+		(sysctl-name "kern.osrelease")
+		(profile-flag "common-exception-entitlement-rules")
+		(extension "com.apple.security.exception.sysctl.read-only")
+	)
+)
+(allow sysctl-read
+	(require-all
+		(require-any
+			(sysctl-name "vm.all_map_ranges")
+			(sysctl-name "vm.vm_map_user_range_debug")
+		)
+		(profile-flag "common-debugging-rules")
+		(require-any
+			(require-all
+				(profile-flag "common-exception-entitlement-rules")
+				(extension "com.apple.security.exception.sysctl.read-only")
+			)
+			(system-attribute developer-mode)
+		)
+	)
+)
 (allow sysctl-read
 	(require-all
 		(profile-flag "common-sysctl-rules")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(require-any
-						(sysctl-name "hw.busfrequency")
-						(sysctl-name "hw.busfrequency_compat")
-						(sysctl-name "hw.cpu64bit_capable")
-						(sysctl-name "hw.cpufrequency")
-						(sysctl-name "hw.cpufrequency_compat")
-						(sysctl-name "hw.cpufrequency_max")
-						(sysctl-name "hw.cpusubtype")
-						(sysctl-name "hw.l1dcachesize_compat")
-						(sysctl-name "hw.l1icachesize_compat")
-						(sysctl-name "hw.l2cachesize_compat")
-						(sysctl-name "hw.l2settings")
-						(sysctl-name "hw.l3cachesize_compat")
-						(sysctl-name "hw.l3settings")
-						(sysctl-name "hw.tbfrequency")
-						(sysctl-name "hw.usermem")
-						(sysctl-name "kern.clockrate")
-						(sysctl-name "kern.development")
-						(sysctl-name "kern.hostid")
-						(sysctl-name "kern.maxproc")
-						(sysctl-name "kern.maxvnodes")
-						(sysctl-name "kern.monotonicclock*")
-						(sysctl-name "kern.monotoniclock_offset_usecs")
-						(sysctl-name "kern.ngroups")
-						(sysctl-name "kern.saved_ids")
-						(sysctl-name "kern.usrstack")
-						(sysctl-name "kern.usrstack64")
-						(sysctl-name "kern.waketime")
-						(sysctl-name "kern.wq_limit_cooperative_threads")
-						(sysctl-name "machdep.virtual_address_size")
-						(sysctl-name "security.mac.amfi.developer_mode_status")
-						(sysctl-name "security.mac.sandbox.sentinel")
-						(sysctl-name "sysctl.proc_translated")
-						(sysctl-name "vm.loadavg")
-					)
 					(sysctl-name "kern.willshutdown")
 					(sysctl-name "kern.willuserspacereboot")
+					(sysctl-name "vm.malloc_ranges")
 				)
 			)
 			(require-all

 				(require-any
 					(require-all
 						(profile-flag "common-exception-entitlement-rules")
-						(extension "com.apple.security.exception.sysctl.read-write")
+						(extension "com.apple.security.exception.sysctl.read-only")
 					)
 					(signing-identifier "com.apple.*")
 				)
 			)
 			(require-any
 				(sysctl-name "hw.activecpu")
+				(sysctl-name "hw.machine")
+				(sysctl-name "hw.memsize")
 				(sysctl-name "hw.ncpu")
+				(sysctl-name "kern.osproductversion")
 				(sysctl-name "kern.osvariant_status")
 				(sysctl-name "kern.secure_kernel")
 			)

 				(sysctl-name "hw.physicalcpu_max")
 				(sysctl-name "hw.product")
 			)
-			(require-any
-				(sysctl-name "hw.machine")
-				(sysctl-name "kern.osproductversion")
-			)
 			(require-any
 				(sysctl-name "kern.hostname")
+				(sysctl-name "kern.ostype")
 				(sysctl-name "kern.version")
 			)
 			(require-any

 				(sysctl-name "kern.osversion")
 			)
 			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
 			(sysctl-name "hw.target")

 			(sysctl-name "kern.boottime")
 			(sysctl-name "kern.osrelease")
 			(sysctl-name "kern.osreleasetype")
-			(sysctl-name "kern.ostype")
 			(sysctl-name "machdep.ptrauth_enabled")
 			(sysctl-name "security.mac.lockdown_mode_state")
 			(sysctl-name "vm.malloc_ranges")
 		)
 	)
 )
-(allow sysctl-read
-	(require-all
-		(sysctl-name "vm.task_no_footprint_for_debug")
-		(profile-flag "common-exception-entitlement-rules")
-		(extension "com.apple.security.exception.sysctl.read-write")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "vm.debug_range_enabled")
-		(profile-flag "common-debugging-rules")
-		(require-any
-			(require-all
-				(profile-flag "common-exception-entitlement-rules")
-				(extension "com.apple.security.exception.sysctl.read-write")
-			)
-			(system-attribute developer-mode)
-		)
-	)
-)
-(allow sysctl-read
-	(require-all
-		(profile-flag "common-exception-entitlement-rules")
-		(extension "com.apple.security.exception.sysctl.read-write")
-	)
-)
 (allow sysctl-read
 	(require-all
 		(sysctl-name "kern.wq_limit_cooperative_threads")

 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.exception.process-info")
 				(require-any
-					(extension "com.apple.security.exception.sysctl.read-write")
+					(extension "com.apple.security.exception.sysctl.read-only")
 					(require-any
 						(sysctl-name "kern.proc.*")
 						(sysctl-name "kern.procargs2.*")

 )
 (allow sysctl-read
 	(require-all
-		(sysctl-name "vm.footprint_suspend")
 		(profile-flag "common-exception-entitlement-rules")
 		(extension "com.apple.security.exception.sysctl.read-write")
 	)
 )
 (allow sysctl-read
 	(require-all
-		(require-any
-			(sysctl-name "vm.all_map_ranges")
-			(sysctl-name "vm.vm_map_user_range_debug")
-		)
+		(sysctl-name "vm.debug_range_enabled")
 		(require-any
 			(require-all
 				(profile-flag "common-debugging-rules")
 				(require-any
 					(require-all
 						(profile-flag "common-exception-entitlement-rules")
-						(extension "com.apple.security.exception.sysctl.read-write")
+						(extension "com.apple.security.exception.sysctl.read-only")
 					)
 					(system-attribute developer-mode)
 				)
 			)
 			(require-all
 				(profile-flag "common-exception-entitlement-rules")
-				(extension "com.apple.security.exception.sysctl.read-write")
+				(extension "com.apple.security.exception.sysctl.read-only")
 			)
 		)
 	)
```
