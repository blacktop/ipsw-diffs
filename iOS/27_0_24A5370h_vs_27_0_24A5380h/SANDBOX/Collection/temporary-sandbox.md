## temporary-sandbox

> Group: ⬆️ Updated

```diff

 ))
 (define (_g3 _)
 	(require-all
-	(subpath "/private/var/PersonaVolumes")
+	(subpath "${FRONT_USER_HOME}")
 	(require-any
 		(_g2 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
 (define (_g4 _)

 			(require-any
 				(require-all
 					(%entitlement-is-present "com.apple.security.system-group-containers")
+					(signing-identifier "com.apple.bookassetd")
+					(_g7 "")
+				)
+				(require-all
+					(%entitlement-is-present "com.apple.security.system-groups")
 					(require-any
 						(_g6 "")
 						(require-all

 						)
 					)
 				)
-				(require-all
-					(%entitlement-is-present "com.apple.security.system-groups")
-					(signing-identifier "com.apple.bookassetd")
-					(_g7 "")
-				)
 				(require-all
 					(signing-identifier "com.apple.appplaceholdersyncd")
 					(subpath "/private/var")

 	(require-any
 		(require-all
 			(%entitlement-is-present "com.apple.security.system-group-containers")
+			(signing-identifier "com.apple.bookassetd")
+			(_g16 "")
+		)
+		(require-all
+			(%entitlement-is-present "com.apple.security.system-groups")
 			(require-any
 				(_g15 "")
 				(require-all

 				)
 			)
 		)
-		(require-all
-			(%entitlement-is-present "com.apple.security.system-groups")
-			(signing-identifier "com.apple.bookassetd")
-			(_g16 "")
-		)
 		(require-all
 			(signing-identifier "com.apple.appplaceholdersyncd")
 			(subpath "/private/var")

 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g20 _)
 	(require-any
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
 (define (_g21 _)

 	(_g20 "")
 ))
 (define (_g22 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
-							(_g20 "")
-						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(_g19 "")
-								(extension "com.apple.mediaserverd.read")
-							)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g20 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g19 "")
+							(extension "com.apple.mediaserverd.read")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g23 _)
 	(require-all
 	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(_g22 "")
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g22 "")
+		)
 		(require-all
 			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 			(require-any
-				(_g22 "")
 				(extension-class "com.apple.mediaserverd.read")
 				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g22 "")
+				)
 			)
 		)
 		(subpath "${HOME}/Library/com.apple.momentsd")

 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g25 _)
 	(require-any
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
 (define (_g26 _)

 	(_g25 "")
 ))
 (define (_g27 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
-							(_g25 "")
-						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(_g24 "")
-								(extension "com.apple.mediaserverd.read")
-							)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g25 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g24 "")
+							(extension "com.apple.mediaserverd.read")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g28 _)
 	(require-all
 	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(_g27 "")
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g27 "")
+		)
 		(require-all
 			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 			(require-any
-				(_g27 "")
 				(extension-class "com.apple.mediaserverd.read")
 				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g27 "")
+				)
 			)
 		)
 		(subpath "${HOME}/Library/com.apple.momentsd")

 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g30 _)
 	(require-any
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
 (define (_g31 _)

 	(_g30 "")
 ))
 (define (_g32 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
-							(_g30 "")
-						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(_g29 "")
-								(extension "com.apple.mediaserverd.read")
-							)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g30 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g29 "")
+							(extension "com.apple.mediaserverd.read")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g33 _)
 	(require-all
 	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(_g32 "")
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g32 "")
+		)
 		(require-all
 			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 			(require-any
-				(_g32 "")
 				(extension-class "com.apple.mediaserverd.read")
 				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g32 "")
+				)
 			)
 		)
 		(subpath "${HOME}/Library/com.apple.momentsd")

 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g35 _)
 	(require-any
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
 (define (_g36 _)

 	(_g35 "")
 ))
 (define (_g37 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
-							(_g35 "")
-						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(_g34 "")
-								(extension "com.apple.mediaserverd.read")
-							)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g35 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g34 "")
+							(extension "com.apple.mediaserverd.read")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g38 _)
 	(require-all
 	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(_g37 "")
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g37 "")
+		)
 		(require-all
 			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 			(require-any
-				(_g37 "")
 				(extension-class "com.apple.mediaserverd.read")
 				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g37 "")
+				)
 			)
 		)
 		(subpath "${HOME}/Library/com.apple.momentsd")

 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g40 _)
 	(require-any
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
 (define (_g41 _)

 	(_g40 "")
 ))
 (define (_g42 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
-							(_g40 "")
-						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(_g39 "")
-								(extension "com.apple.mediaserverd.read")
-							)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g40 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g39 "")
+							(extension "com.apple.mediaserverd.read")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g43 _)
 	(require-all
 	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(_g42 "")
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g42 "")
+		)
 		(require-all
 			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 			(require-any
-				(_g42 "")
 				(extension-class "com.apple.mediaserverd.read")
 				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g42 "")
+				)
 			)
 		)
 		(subpath "${HOME}/Library/com.apple.momentsd")

 								(_g39 "")
 								(_g41 "")
 								(require-all
-									(subpath "/private/var")
+									(require-any
+										(subpath "${FRONT_USER_HOME}")
+										(subpath "${HOME}")
+									)
 									(require-any
 										(_g41 "")
 										(require-all
-											(require-any
-												(subpath "${FRONT_USER_HOME}")
-												(subpath "${HOME}")
-											)
+											(subpath "/private/var")
 											(require-any
 												(_g41 "")
 												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")

 	(require-any
 		(require-all
 			(%entitlement-is-present "com.apple.security.system-group-containers")
+			(signing-identifier "com.apple.bookassetd")
+			(_g48 "")
+		)
+		(require-all
+			(%entitlement-is-present "com.apple.security.system-groups")
 			(require-any
 				(_g47 "")
 				(require-all

 				)
 			)
 		)
-		(require-all
-			(%entitlement-is-present "com.apple.security.system-groups")
-			(signing-identifier "com.apple.bookassetd")
-			(_g48 "")
-		)
 		(require-all
 			(signing-identifier "com.apple.appplaceholdersyncd")
 			(subpath "/private/var")

 	)
 ))
 (define (_g50 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(require-any
 							(require-any
-								(require-any
-									(subpath "/AppleInternal/Applications")
-									(subpath "/System/Developer/Applications")
-								)
-								(require-any
-									(subpath "/private/var/factory_mount/[^/]+/Applications")
-									(subpath "/private/var/personalized_automation/Applications")
-									(subpath "/private/var/personalized_debug/Applications")
-									(subpath "/private/var/personalized_factory/[^/]+/Applications")
-								)
-								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-								(subpath "/Applications")
-								(subpath "/Developer/Applications")
-								(subpath "/private/var/containers/Bundle")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(extension "com.apple.mediaserverd.read")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-							)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(extension "com.apple.mediaserverd.read")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g51 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(require-any
 							(require-any
-								(require-any
-									(subpath "/AppleInternal/Applications")
-									(subpath "/System/Developer/Applications")
-								)
-								(require-any
-									(subpath "/private/var/factory_mount/[^/]+/Applications")
-									(subpath "/private/var/personalized_automation/Applications")
-									(subpath "/private/var/personalized_debug/Applications")
-									(subpath "/private/var/personalized_factory/[^/]+/Applications")
-								)
-								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-								(subpath "/Applications")
-								(subpath "/Developer/Applications")
-								(subpath "/private/var/containers/Bundle")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(extension "com.apple.mediaserverd.read")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-							)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(extension "com.apple.mediaserverd.read")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g52 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(require-any
 							(require-any
-								(require-any
-									(subpath "/AppleInternal/Applications")
-									(subpath "/System/Developer/Applications")
-								)
-								(require-any
-									(subpath "/private/var/factory_mount/[^/]+/Applications")
-									(subpath "/private/var/personalized_automation/Applications")
-									(subpath "/private/var/personalized_debug/Applications")
-									(subpath "/private/var/personalized_factory/[^/]+/Applications")
-								)
-								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-								(subpath "/Applications")
-								(subpath "/Developer/Applications")
-								(subpath "/private/var/containers/Bundle")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(extension "com.apple.mediaserverd.read")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-							)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(extension "com.apple.mediaserverd.read")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g53 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.mediaplaybackd")
-			(require-any
-				(extension "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.mediaserverd.read")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.linkd")
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(require-any
 							(require-any
-								(require-any
-									(subpath "/AppleInternal/Applications")
-									(subpath "/System/Developer/Applications")
-								)
-								(require-any
-									(subpath "/private/var/factory_mount/[^/]+/Applications")
-									(subpath "/private/var/personalized_automation/Applications")
-									(subpath "/private/var/personalized_debug/Applications")
-									(subpath "/private/var/personalized_factory/[^/]+/Applications")
-								)
-								(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-								(subpath "/Applications")
-								(subpath "/Developer/Applications")
-								(subpath "/private/var/containers/Bundle")
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
 						)
-						(require-all
-							(signing-identifier "com.apple.mediaplaybackd")
-							(require-any
-								(extension "com.apple.mediaserverd.read")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-							)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(extension "com.apple.mediaserverd.read")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 						)
 					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g54 _)
 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g55 _)
 	(require-any
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
 (define (_g56 _)

 	(_g59 "")
 ))
 (define (_g61 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(_g59 "")
+))
+(define (_g62 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read")
 	(signing-identifier "com.apple.linkd")
 	(_g55 "")
 ))
-(define (_g62 _)
+(define (_g63 _)
 	(require-any
 	(_g54 "")
-	(_g61 "")
+	(_g62 "")
 	(require-all
-		(subpath "/private/var")
 		(require-any
-			(_g61 "")
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(require-any
+			(_g62 "")
 			(require-all
+				(subpath "/private/var")
 				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(require-any
-					(_g61 "")
+					(_g62 "")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 				)
 			)
 		)
 	)
 ))
-(define (_g63 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.mediaplaybackd")
-	(_g62 "")
-))
 (define (_g64 _)
 	(require-all
 	(extension-class "com.apple.aned.read-only")

 	(_g68 "")
 ))
 (define (_g72 _)
+	(extension "com.apple.security.exception.files.home-relative-path.read-write"))
+(define (_g73 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read-write")
-	(extension "com.apple.security.exception.files.home-relative-path.read-write")
+	(require-any
+		(_g72 "")
+		(extension "com.apple.security.exception.files.absolute-path.read-write")
+	)
 ))
-(define (_g73 _)
+(define (_g74 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read-write")
 	(extension "com.apple.app-sandbox.read-write")
 ))
-(define (_g74 _)
-	(require-any
-	(_g73 "")
-	(extension "com.apple.clouddocs.version")
-))
 (define (_g75 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
 	(require-any
-		(_g73 "")
-		(require-all
-			(vnode-type REGULAR-FILE)
-			(_g74 "")
-		)
-	)
+	(_g74 "")
+	(extension "com.apple.clouddocs.version")
 ))
 (define (_g76 _)
 	(require-all
-	(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
-	(vnode-type REGULAR-FILE)
-	(_g74 "")
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+	(require-any
+		(_g74 "")
+		(require-all
+			(vnode-type REGULAR-FILE)
+			(_g75 "")
+		)
+	)
 ))
 (define (_g77 _)
+	(require-all
+	(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
+	(vnode-type REGULAR-FILE)
+	(_g75 "")
+))
+(define (_g78 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read-write")
 	(extension "com.apple.app-sandbox.read-write")
 ))
-(define (_g78 _)
+(define (_g79 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 									(extension "com.apple.security.exception.files.absolute-path.read-only")
 									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 								)
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
 								(require-all
 									(extension "com.apple.security.exception.files.home-relative-path.read-only")
 									(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 								)
 							)
 						)
-						(require-any
-							(subpath "/AppleInternal/Applications")
-							(subpath "/System/Developer/Applications")
-						)
 						(require-any
 							(subpath "/private/var/factory_mount/[^/]+/Applications")
 							(subpath "/private/var/personalized_automation/Applications")

 							(subpath "/private/var/personalized_factory/[^/]+/Applications")
 						)
 						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/AppleInternal/Applications")
 						(subpath "/Applications")
 						(subpath "/Developer/Applications")
+						(subpath "/System/Developer/Applications")
 						(subpath "/private/var/containers/Bundle")
 					)
 				)

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
-(define (_g79 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes")
-	(require-any
-		(_g78 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
 (define (_g80 _)
 	(require-all
-	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(subpath "/private/var/PersonaVolumes")
 	(require-any
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 		(require-all
-			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(subpath "${FRONT_USER_HOME}")
 			(require-any
-				(require-all
-					(extension-class "com.apple.app-sandbox.read")
-					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-					(require-any
-						(require-all
-							(extension-class "com.apple.mediaserverd.read")
-							(require-any
-								(require-all
-									(extension "com.apple.security.exception.files.absolute-path.read-only")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.home-relative-path.read-only")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.home-relative-path.read-write")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-							)
-						)
-						(require-any
-							(subpath "/AppleInternal/Applications")
-							(subpath "/System/Developer/Applications")
-						)
-						(require-any
-							(subpath "/private/var/factory_mount/[^/]+/Applications")
-							(subpath "/private/var/personalized_automation/Applications")
-							(subpath "/private/var/personalized_debug/Applications")
-							(subpath "/private/var/personalized_factory/[^/]+/Applications")
-						)
-						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-						(subpath "/Applications")
-						(subpath "/Developer/Applications")
-						(subpath "/private/var/containers/Bundle")
-					)
-				)
-				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-				)
+				(_g79 "")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 			)
 		)
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
 (define (_g81 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(require-any
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-		(require-all
-			(subpath "/private/var/PersonaVolumes")
-			(require-any
-				(_g80 "")
-				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-			)
-		)
-	)
-))
-(define (_g82 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes")
-	(require-any
-		(_g81 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
-(define (_g83 _)
-	(require-all
-	(extension-class "com.apple.mediaserverd.read")
-	(require-any
-		(_g80 "")
-		(require-all
-			(subpath "/private/var")
-			(require-any
-				(_g80 "")
-				(require-all
-					(extension "com.apple.sandbox.application-group")
-					(require-any
-						(_g81 "")
-						(_g82 "")
-						(require-all
-							(subpath "${FRONT_USER_HOME}")
-							(require-any
-								(_g82 "")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-))
-(define (_g84 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 									(extension "com.apple.security.exception.files.absolute-path.read-only")
 									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 								)
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
 								(require-all
 									(extension "com.apple.security.exception.files.home-relative-path.read-only")
 									(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 								)
 							)
 						)
-						(require-any
-							(subpath "/AppleInternal/Applications")
-							(subpath "/System/Developer/Applications")
-						)
 						(require-any
 							(subpath "/private/var/factory_mount/[^/]+/Applications")
 							(subpath "/private/var/personalized_automation/Applications")

 							(subpath "/private/var/personalized_factory/[^/]+/Applications")
 						)
 						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/AppleInternal/Applications")
 						(subpath "/Applications")
 						(subpath "/Developer/Applications")
+						(subpath "/System/Developer/Applications")
 						(subpath "/private/var/containers/Bundle")
 					)
 				)

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
+(define (_g82 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g81 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g83 _)
+	(require-any
+	(_g82 "")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+))
+(define (_g84 _)
+	(require-all
+	(subpath "/private/var")
+	(extension "com.apple.sandbox.application-group")
+	(require-any
+		(require-all
+			(extension-class "com.apple.aned.read-only")
+			(require-any
+				(_g81 "")
+				(_g82 "")
+				(require-all
+					(subpath "/private/var/PersonaVolumes")
+					(_g83 "")
+				)
+			)
+		)
+		(require-all
+			(extension-class "com.apple.app-sandbox.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g83 "")
+		)
+		(require-all
+			(extension-class "com.apple.mediaserverd.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g83 "")
+		)
+	)
+))
 (define (_g85 _)
 	(require-all
 	(subpath "${FRONT_USER_HOME}")
 	(require-any
+		(_g84 "")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-		(require-all
-			(subpath "/private/var/PersonaVolumes")
-			(require-any
-				(_g84 "")
-				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-			)
-		)
 	)
 ))
 (define (_g86 _)
 	(require-all
-	(subpath "/private/var/PersonaVolumes")
+	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g85 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(_g81 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g81 "")
+				(require-all
+					(extension "com.apple.sandbox.application-group")
+					(require-any
+						(_g84 "")
+						(_g85 "")
+						(require-all
+							(subpath "/private/var/PersonaVolumes")
+							(require-any
+								(_g85 "")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
 	)
 ))
 (define (_g87 _)
 	(require-all
-	(extension-class "com.apple.mediaserverd.read")
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any
-		(_g84 "")
 		(require-all
-			(subpath "/private/var")
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
 			(require-any
-				(_g84 "")
 				(require-all
-					(extension "com.apple.sandbox.application-group")
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 					(require-any
-						(_g85 "")
-						(_g86 "")
 						(require-all
-							(subpath "${FRONT_USER_HOME}")
+							(extension-class "com.apple.mediaserverd.read")
 							(require-any
-								(_g86 "")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
 							)
 						)
+						(require-any
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/AppleInternal/Applications")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/System/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
 					)
 				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
 			)
 		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
 (define (_g88 _)
 	(require-all
-	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(require-all
-			(%entitlement-is-present "com.apple.security.ts.tmpdir")
-			(require-any
-				(require-all
-					(extension-class "com.apple.app-sandbox.read")
-					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-					(require-any
-						(require-all
-							(extension-class "com.apple.mediaserverd.read")
-							(require-any
-								(require-all
-									(extension "com.apple.security.exception.files.absolute-path.read-only")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.home-relative-path.read-only")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.home-relative-path.read-write")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-							)
-						)
-						(require-any
-							(subpath "/AppleInternal/Applications")
-							(subpath "/System/Developer/Applications")
-						)
-						(require-any
-							(subpath "/private/var/factory_mount/[^/]+/Applications")
-							(subpath "/private/var/personalized_automation/Applications")
-							(subpath "/private/var/personalized_debug/Applications")
-							(subpath "/private/var/personalized_factory/[^/]+/Applications")
-						)
-						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-						(subpath "/Applications")
-						(subpath "/Developer/Applications")
-						(subpath "/private/var/containers/Bundle")
-					)
-				)
-				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-				)
-			)
-		)
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+		(_g87 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
 (define (_g89 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-		(require-all
-			(subpath "/private/var/PersonaVolumes")
-			(require-any
-				(_g88 "")
-				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-			)
-		)
-	)
+	(_g88 "")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
 (define (_g90 _)
 	(require-all
-	(subpath "/private/var/PersonaVolumes")
+	(subpath "/private/var")
+	(extension "com.apple.sandbox.application-group")
 	(require-any
-		(_g89 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(require-all
+			(extension-class "com.apple.aned.read-only")
+			(require-any
+				(_g87 "")
+				(_g88 "")
+				(require-all
+					(subpath "/private/var/PersonaVolumes")
+					(_g89 "")
+				)
+			)
+		)
+		(require-all
+			(extension-class "com.apple.app-sandbox.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g89 "")
+		)
+		(require-all
+			(extension-class "com.apple.mediaserverd.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g89 "")
+		)
 	)
 ))
 (define (_g91 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g90 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g92 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g88 "")
+		(_g87 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g88 "")
+				(_g87 "")
 				(require-all
 					(extension "com.apple.sandbox.application-group")
 					(require-any
-						(_g89 "")
 						(_g90 "")
+						(_g91 "")
 						(require-all
-							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes")
 							(require-any
-								(_g90 "")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(_g91 "")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)
 					)

 		)
 	)
 ))
-(define (_g92 _)
+(define (_g93 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 									(extension "com.apple.security.exception.files.absolute-path.read-only")
 									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 								)
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
 								(require-all
 									(extension "com.apple.security.exception.files.home-relative-path.read-only")
 									(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 								)
 							)
 						)
-						(require-any
-							(subpath "/AppleInternal/Applications")
-							(subpath "/System/Developer/Applications")
-						)
 						(require-any
 							(subpath "/private/var/factory_mount/[^/]+/Applications")
 							(subpath "/private/var/personalized_automation/Applications")

 							(subpath "/private/var/personalized_factory/[^/]+/Applications")
 						)
 						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/AppleInternal/Applications")
 						(subpath "/Applications")
 						(subpath "/Developer/Applications")
+						(subpath "/System/Developer/Applications")
 						(subpath "/private/var/containers/Bundle")
 					)
 				)

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
-(define (_g93 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes")
-	(require-any
-		(_g92 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
 (define (_g94 _)
 	(require-all
 	(subpath "${FRONT_USER_HOME}")

 	)
 ))
 (define (_g95 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes")
 	(require-any
-		(_g94 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
+	(_g94 "")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
 (define (_g96 _)
+	(require-all
+	(subpath "/private/var")
+	(extension "com.apple.sandbox.application-group")
+	(require-any
+		(require-all
+			(extension-class "com.apple.aned.read-only")
+			(require-any
+				(_g93 "")
+				(_g94 "")
+				(require-all
+					(subpath "/private/var/PersonaVolumes")
+					(_g95 "")
+				)
+			)
+		)
+		(require-all
+			(extension-class "com.apple.app-sandbox.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g95 "")
+		)
+		(require-all
+			(extension-class "com.apple.mediaserverd.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g95 "")
+		)
+	)
+))
+(define (_g97 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g96 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g98 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g92 "")
+		(_g93 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g92 "")
+				(_g93 "")
 				(require-all
 					(extension "com.apple.sandbox.application-group")
 					(require-any
-						(_g94 "")
-						(_g95 "")
+						(_g96 "")
+						(_g97 "")
 						(require-all
-							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes")
 							(require-any
-								(_g95 "")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(_g97 "")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)
 					)

 		)
 	)
 ))
-(define (_g97 _)
+(define (_g99 _)
+	(require-all
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any
-	(_g92 "")
-	(_g93 "")
-	(_g94 "")
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/AppleInternal/Applications")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/System/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
 ))
-(define (_g98 _)
+(define (_g100 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g99 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g101 _)
+	(require-any
+	(_g100 "")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+))
+(define (_g102 _)
+	(require-all
+	(subpath "/private/var")
+	(extension "com.apple.sandbox.application-group")
+	(require-any
+		(require-all
+			(extension-class "com.apple.aned.read-only")
+			(require-any
+				(_g100 "")
+				(_g99 "")
+				(require-all
+					(subpath "/private/var/PersonaVolumes")
+					(_g101 "")
+				)
+			)
+		)
+		(require-all
+			(extension-class "com.apple.app-sandbox.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g101 "")
+		)
+		(require-all
+			(extension-class "com.apple.mediaserverd.read")
+			(subpath "/private/var/PersonaVolumes")
+			(_g101 "")
+		)
+	)
+))
+(define (_g103 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g102 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g104 _)
+	(require-all
+	(extension-class "com.apple.mediaserverd.read")
+	(require-any
+		(_g99 "")
+		(require-all
+			(subpath "/private/var")
+			(require-any
+				(_g99 "")
+				(require-all
+					(extension "com.apple.sandbox.application-group")
+					(require-any
+						(_g102 "")
+						(_g103 "")
+						(require-all
+							(subpath "/private/var/PersonaVolumes")
+							(require-any
+								(_g103 "")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+))
+(define (_g105 _)
 	(require-all
 	(extension "com.apple.security.exception.files.home-relative-path.read-write")
 	(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 ))
-(define (_g99 _)
+(define (_g106 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g98 "")
+		(_g105 "")
 		(require-all
 			(extension "com.apple.security.exception.files.absolute-path.read-only")
 			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 		)
+		(require-all
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+		)
 		(require-all
 			(extension "com.apple.security.exception.files.home-relative-path.read-only")
 			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 		)
 	)
 ))
-(define (_g100 _)
+(define (_g107 _)
 	(require-any
-	(_g99 "")
-	(require-any
-		(subpath "/AppleInternal/Applications")
-		(subpath "/System/Developer/Applications")
-	)
+	(_g106 "")
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 		(subpath "/private/var/personalized_factory/[^/]+/Applications")
 	)
 	(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+	(subpath "/AppleInternal/Applications")
 	(subpath "/Applications")
 	(subpath "/Developer/Applications")
+	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g101 _)
+(define (_g108 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read")
 	(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-	(_g100 "")
+	(_g107 "")
 ))
-(define (_g102 _)
+(define (_g109 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.tmpdir")
 	(require-any
-		(_g101 "")
+		(_g108 "")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
 			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
 		)
 	)
 ))
-(define (_g103 _)
-	(require-all
-	(extension-class "com.apple.mediaserverd.read-write")
-	(require-any
-		(require-all
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-		)
-		(require-all
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-		)
-	)
-))
-(define (_g104 _)
+(define (_g110 _)
 	(require-all
+	(extension-class "com.apple.aned.read-only")
+	(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
 	(extension "com.apple.assets.read")
 	(require-any
-		(require-all
-			(subpath "${HOME}/Library/Assets")
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-		)
-		(require-all
-			(subpath "/private/var/MobileAsset")
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-		)
+		(subpath "${HOME}/Library/Assets")
+		(subpath "/private/var/MobileAsset")
 	)
 ))
 (allow file-issue-extension

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
-			(_g72 "")
-			(_g77 "")
+			(_g73 "")
+			(_g78 "")
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(extension "com.apple.librarian.ubiquity-container")
 				(require-any
-					(_g72 "")
+					(_g73 "")
 					(require-all
 						(subpath "${HOME}/Library/Mobile Documents")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g72 "")
+							(_g73 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 								(require-any
-									(_g72 "")
+									(_g73 "")
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
 										(require-any

 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 				)
 			)

 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(require-any
+					(_g72 "")
 					(extension "com.apple.app-sandbox.read-write")
 					(extension "com.apple.security.exception.files.absolute-path.read-only")
 					(extension "com.apple.security.exception.files.absolute-path.read-write")
 					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
 				)
 			)
 			(require-all
 				(extension-class "com.apple.quicklook.readonly")
 				(require-any
-					(_g73 "")
-					(_g75 "")
+					(_g74 "")
 					(_g76 "")
 					(_g77 "")
+					(_g78 "")
 					(require-all
 						(extension-class "com.apple.mediaserverd.read")
 						(extension "com.apple.app-sandbox.read-write")

 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g76 "")
+							(_g77 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
 								(require-any
-									(_g75 "")
+									(_g76 "")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-				(extension-class "com.apple.quicklook.readonly")
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 				(require-any
+					(extension-class "com.apple.aned.read-only")
+					(extension-class "com.apple.app-sandbox.read")
+					(extension-class "com.apple.app-sandbox.read-write")
 					(extension-class "com.apple.mediaserverd.read")
 					(extension-class "com.apple.mediaserverd.read-write")
 					(extension-class "com.apple.quicklook.readonly")
 				)
 			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
 		)
 	)
 	(require-all

 					(_g71 "")
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
+						(signing-identifier "com.apple.bookassetd")
+						(_g70 "")
+					)
+					(require-all
+						(%entitlement-is-present "com.apple.security.system-groups")
 						(require-any
 							(_g69 "")
 							(require-all

 							)
 						)
 					)
-					(require-all
-						(%entitlement-is-present "com.apple.security.system-groups")
-						(signing-identifier "com.apple.bookassetd")
-						(_g70 "")
-					)
 				)
 			)
 		)

 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(extension "com.apple.assets.read")
 		(require-any
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
-				(require-any
-					(require-all
-						(extension-class "com.apple.app-sandbox.read")
-						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-						(require-any
-							(require-all
-								(extension-class "com.apple.mediaserverd.read")
-								(require-any
-									(require-all
-										(extension "com.apple.security.exception.files.absolute-path.read-only")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-									(require-all
-										(extension "com.apple.security.exception.files.home-relative-path.read-only")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-									(require-all
-										(extension "com.apple.security.exception.files.home-relative-path.read-write")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-								)
-							)
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-							)
-							(require-any
-								(subpath "/private/var/factory_mount/[^/]+/Applications")
-								(subpath "/private/var/personalized_automation/Applications")
-								(subpath "/private/var/personalized_debug/Applications")
-								(subpath "/private/var/personalized_factory/[^/]+/Applications")
-							)
-							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-							(subpath "/Applications")
-							(subpath "/Developer/Applications")
-							(subpath "/private/var/containers/Bundle")
-						)
-					)
-					(require-any
-						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					)
-				)
+				(subpath "${HOME}/Library/Assets")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(subpath "/private/var/MobileAsset")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 			)
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 		)
 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(extension "com.apple.sandbox.container")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+			(_g108 "")
+			(_g109 "")
+			(require-all
+				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+				(require-any
+					(_g109 "")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+				)
+			)
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(require-any
+					(_g106 "")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+						(_g107 "")
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+				(_g107 "")
+			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(require-any
+					(_g105 "")
 					(require-all
 						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-					(require-all
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+						(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 					)
 				)
 			)

 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-		(signing-identifier "com.apple.storagedatad")
+		(require-any
+			(_g11 "")
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(require-any
+					(require-all
+						(require-any
+							(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+						)
+						(signing-identifier "com.apple.chronod")
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(subpath "/private/var")
+						(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+						(signing-identifier "com.apple.chronod")
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+				)
+				(signing-identifier "com.apple.chronod")
+			)
+			(require-all
+				(signing-identifier "com.apple.cloudpaird")
+				(require-any
+					(_g11 "")
+					(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+				)
+			)
+		)
 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(_g78 "")
+			(_g44 "")
+			(require-all
+				(signing-identifier "com.apple.anomalydetectiond")
+				(require-any
+					(_g44 "")
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(_g60 "")
+			(_g61 "")
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(require-any
+					(_g58 "")
+					(_g64 "")
+					(require-all
+						(extension-class "com.apple.app-sandbox.read")
+						(require-any
+							(_g62 "")
+							(_g64 "")
+							(require-all
+								(extension-class "com.apple.mediaserverd.read")
+								(signing-identifier "com.apple.linkd")
+								(_g55 "")
+							)
+							(require-all
+								(signing-identifier "com.apple.mediaplaybackd")
+								(_g63 "")
+							)
+						)
+					)
+					(require-all
+						(extension-class "com.apple.app-sandbox.read-write")
+						(signing-identifier "com.apple.mediaplaybackd")
+						(_g63 "")
+					)
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(require-any
+							(_g56 "")
+							(require-all
+								(extension-class "com.apple.mediaserverd.read-write")
+								(signing-identifier "com.apple.mediaplaybackd")
+								(_g63 "")
+							)
+							(require-all
+								(signing-identifier "com.apple.mediaplaybackd")
+								(_g57 "")
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.momentsd")
+						(_g59 "")
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(signing-identifier "com.apple.momentsd")
+				(_g59 "")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(signing-identifier "com.apple.momentsd")
+				(_g59 "")
+			)
+			(require-all
+				(signing-identifier "com.apple.momentsd")
+				(require-any
+					(_g61 "")
+					(require-all
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(require-any
+							(_g60 "")
+							(extension-class "com.apple.mediaserverd.read")
+							(extension-class "com.apple.mediaserverd.read-write")
+						)
+					)
+					(subpath "${HOME}/Library/com.apple.momentsd")
+				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(_g79 "")
 			(require-all
 				(extension "com.apple.sandbox.application-group")
 				(require-any
-					(_g78 "")
+					(_g79 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-								(require-any
-									(_g79 "")
-									(subpath "${FRONT_USER_HOME}")
-								)
-							)
+							(_g80 "")
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
 								(require-any
-									(_g79 "")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(_g80 "")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 								)
 							)
 						)

 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
+			(_g9 "")
+			(require-all
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+				(signing-identifier "com.apple.storagedatad")
+			)
 			(require-all
-				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g38 "")
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(require-any
+					(_g9 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g38 "")
+							(_g9 "")
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(signing-identifier "com.apple.MTLAssetUpgraderD")
-									)
-									(require-all
-										(signing-identifier "com.apple.mediaplaybackd")
-										(require-any
-											(_g34 "")
-											(_g36 "")
-											(require-all
-												(subpath "/private/var")
-												(require-any
-													(_g36 "")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(require-any
-															(_g36 "")
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
-														)
-													)
-												)
-											)
-										)
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+								(signing-identifier "com.apple.storagedatad")
 							)
 						)
 					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
 				)
 			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.cloudpaird")
 		(require-any
 			(require-all
-				(extension-class "com.apple.app-sandbox.read")
 				(require-any
-					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
 				)
-				(signing-identifier "com.apple.chronod")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+				(signing-identifier "com.apple.fileindexerd")
 			)
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-		)
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.momentsd")
-		(require-any
-			(_g53 "")
 			(require-all
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-				(require-any
-					(_g53 "")
-					(extension-class "com.apple.mediaserverd.read")
-					(extension-class "com.apple.mediaserverd.read-write")
-				)
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+				(signing-identifier "com.apple.fileindexerd")
 			)
-			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.fileindexerd")
-	)
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 										(extension "com.apple.security.exception.files.absolute-path.read-only")
 										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
 									(require-all
 										(extension "com.apple.security.exception.files.home-relative-path.read-only")
 										(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 									)
 								)
 							)
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-							)
 							(require-any
 								(subpath "/private/var/factory_mount/[^/]+/Applications")
 								(subpath "/private/var/personalized_automation/Applications")

 								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
 							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
 							(subpath "/Applications")
 							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
 							(subpath "/private/var/containers/Bundle")
 						)
 					)

 		(extension-class "com.apple.app-sandbox.read")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g87 "")
+			(_g98 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g87 "")
+					(_g98 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g87 "")
+							(_g98 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-any
-					(require-all
-						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-					(require-all
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-				)
-			)
-		)
-	)
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g28 "")
+					(_g33 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g28 "")
+							(_g33 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g24 "")
-											(_g26 "")
+											(_g29 "")
+											(_g31 "")
 											(require-all
-												(subpath "/private/var")
 												(require-any
-													(_g26 "")
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(_g31 "")
 													(require-all
+														(subpath "/private/var")
 														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(require-any
-															(_g26 "")
+															(_g31 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 		(extension-class "com.apple.app-sandbox.read")
 		(signing-identifier "com.apple.momentsd")
 		(require-any
-			(_g51 "")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.momentsd")
+				(_g52 "")
+			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(require-any
-					(_g51 "")
 					(extension-class "com.apple.mediaserverd.read")
 					(extension-class "com.apple.mediaserverd.read-write")
+					(require-all
+						(extension-class "com.apple.app-sandbox.read-write")
+						(signing-identifier "com.apple.momentsd")
+						(_g52 "")
+					)
 				)
 			)
 			(subpath "${HOME}/Library/com.apple.momentsd")

 										(extension "com.apple.security.exception.files.absolute-path.read-only")
 										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
 									(require-all
 										(extension "com.apple.security.exception.files.home-relative-path.read-only")
 										(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 									)
 								)
 							)
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-							)
 							(require-any
 								(subpath "/private/var/factory_mount/[^/]+/Applications")
 								(subpath "/private/var/personalized_automation/Applications")

 								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
 							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
 							(subpath "/Applications")
 							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
 							(subpath "/private/var/containers/Bundle")
 						)
 					)

 		(extension-class "com.apple.app-sandbox.read-write")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g83 "")
+			(_g92 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g83 "")
+					(_g92 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g83 "")
+							(_g92 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-any
-					(require-all
-						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-					(require-all
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-				)
-			)
-		)
-	)
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
 		(signing-identifier "com.apple.anomalydetectiond")

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g23 "")
+					(_g28 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g23 "")
+							(_g28 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g19 "")
-											(_g21 "")
+											(_g24 "")
+											(_g26 "")
 											(require-all
-												(subpath "/private/var")
 												(require-any
-													(_g21 "")
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(_g26 "")
 													(require-all
+														(subpath "/private/var")
 														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(require-any
-															(_g21 "")
+															(_g26 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 		(extension-class "com.apple.app-sandbox.read-write")
 		(signing-identifier "com.apple.momentsd")
 		(require-any
-			(_g50 "")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.momentsd")
+				(_g51 "")
+			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(require-any
-					(_g50 "")
 					(extension-class "com.apple.mediaserverd.read")
 					(extension-class "com.apple.mediaserverd.read-write")
+					(require-all
+						(extension-class "com.apple.app-sandbox.read-write")
+						(signing-identifier "com.apple.momentsd")
+						(_g51 "")
+					)
 				)
 			)
 			(subpath "${HOME}/Library/com.apple.momentsd")

 					)
 				)
 			)
-			(require-all
-				(signing-identifier "com.apple.announced")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FTLivePhotoService")
-				(signing-identifier "com.apple.FTLivePhotoService")
-				(_g1 "")
-			)
 			(require-all
 				(signing-identifier "com.apple.asktod")
 				(require-any

 									(_g2 "")
 									(_g3 "")
 									(require-all
-										(subpath "${FRONT_USER_HOME}")
+										(subpath "/private/var/PersonaVolumes")
 										(require-any
 											(_g3 "")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 										)
 									)
 								)

 			)
 			(require-all
 				(subpath "${PROCESS_TEMP_DIR}")
-				(require-any
-					(_g2 "")
-					(require-any
-						(signing-identifier "com.apple.internal.livtipsd")
-						(signing-identifier "com.apple.usernotificationsd")
-					)
-					(signing-identifier "com.apple.Carousel")
-					(signing-identifier "com.apple.FTLivePhotoService")
-					(signing-identifier "com.apple.announced")
-					(signing-identifier "com.apple.asktod")
-					(signing-identifier "com.apple.facetimemessagestored")
-				)
+				(signing-identifier "com.apple.FTLivePhotoService")
 			)
 			(require-all
 				(subpath "/private/var")

 			)
 			(require-all
 				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.asktod")
+				(require-any
+					(_g2 "")
+					(require-any
+						(signing-identifier "com.apple.internal.livtipsd")
+						(signing-identifier "com.apple.usernotificationsd")
+					)
+					(signing-identifier "com.apple.Carousel")
+					(signing-identifier "com.apple.FTLivePhotoService")
+					(signing-identifier "com.apple.announced")
+					(signing-identifier "com.apple.asktod")
+					(signing-identifier "com.apple.facetimemessagestored")
+				)
 			)
 		)
 	)

 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 		(require-any
-			(_g101 "")
-			(_g102 "")
 			(require-all
-				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+				(%entitlement-is-present "com.apple.security.ts.tmpdir")
 				(require-any
-					(_g102 "")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-				)
-			)
-			(require-all
-				(extension-class "com.apple.aned.read-only")
-				(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-				(_g100 "")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(_g99 "")
 					(require-all
+						(extension-class "com.apple.app-sandbox.read")
 						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-						(_g100 "")
+						(require-any
+							(require-all
+								(extension-class "com.apple.mediaserverd.read")
+								(require-any
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-only")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+									(require-all
+										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
+								)
+							)
+							(require-any
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
+							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
+						)
 					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-any
-					(_g98 "")
-					(require-all
-						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+					(require-any
+						(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+						(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
 					)
 				)
 			)
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 		)
 	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+		(signing-identifier "com.apple.storagedatad")
+	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(_g103 "")
+			(_g102 "")
+			(_g104 "")
 			(require-all
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-					(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-					(_g103 "")
-				)
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension "com.apple.sandbox.application-group")
 				(require-any
 					(_g104 "")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-						(require-any
-							(_g104 "")
-							(extension "com.apple.security.exception.files.absolute-path.read-only")
-							(extension "com.apple.security.exception.files.absolute-path.read-write")
-							(extension "com.apple.security.exception.files.home-relative-path.read-only")
-							(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						)
-					)
-				)
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(_g11 "")
-			(require-all
-				(extension-class "com.apple.aned.read-only")
-				(require-any
-					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-				)
-				(signing-identifier "com.apple.chronod")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(require-any
-							(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-						)
-						(signing-identifier "com.apple.chronod")
-					)
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-						(signing-identifier "com.apple.chronod")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.cloudpaird")
-				(require-any
-					(_g11 "")
-					(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-				)
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(_g44 "")
-			(require-all
-				(signing-identifier "com.apple.anomalydetectiond")
-				(require-any
-					(_g44 "")
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-				)
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(_g60 "")
-			(require-all
-				(extension-class "com.apple.aned.read-only")
-				(signing-identifier "com.apple.momentsd")
-				(_g59 "")
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(signing-identifier "com.apple.momentsd")
-				(_g59 "")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(_g58 "")
-					(_g63 "")
-					(_g64 "")
-					(require-all
-						(extension-class "com.apple.app-sandbox.read")
-						(signing-identifier "com.apple.mediaplaybackd")
-						(_g62 "")
-					)
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(_g56 "")
-							(_g63 "")
+							(_g104 "")
 							(require-all
-								(signing-identifier "com.apple.mediaplaybackd")
-								(_g57 "")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								(require-any
+									(_g104 "")
+									(subpath "${FRONT_USER_HOME}")
+								)
 							)
 						)
 					)
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(signing-identifier "com.apple.linkd")
-						(_g55 "")
-					)
-					(require-all
-						(extension-class "com.apple.mediaserverd.read-write")
-						(require-any
-							(_g61 "")
-							(_g64 "")
-							(require-all
-								(signing-identifier "com.apple.mediaplaybackd")
-								(_g62 "")
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.momentsd")
-						(_g59 "")
-					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(signing-identifier "com.apple.momentsd")
-				(_g59 "")
-			)
-			(require-all
-				(signing-identifier "com.apple.momentsd")
-				(require-any
-					(_g60 "")
-					(require-all
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-						(require-any
-							(_g60 "")
-							(extension-class "com.apple.mediaserverd.read")
-							(extension-class "com.apple.mediaserverd.read-write")
-						)
-					)
-					(subpath "${HOME}/Library/com.apple.momentsd")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)
 		)

 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(_g9 "")
 			(require-all
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-				(signing-identifier "com.apple.storagedatad")
+				(extension "com.apple.security.exception.files.absolute-path.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 			)
 			(require-all
-				(subpath "/private/var")
-				(require-any
-					(_g9 "")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(_g9 "")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-								(signing-identifier "com.apple.storagedatad")
-							)
-						)
-					)
-				)
+				(extension "com.apple.security.exception.files.absolute-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.home-relative-path.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 			)
 		)
 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
-			(_g96 "")
 			(require-all
-				(extension "com.apple.sandbox.application-group")
+				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g96 "")
+					(_g38 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g96 "")
+							(_g38 "")
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any
-									(_g96 "")
-									(subpath "${FRONT_USER_HOME}")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(signing-identifier "com.apple.MTLAssetUpgraderD")
+									)
+									(require-all
+										(signing-identifier "com.apple.mediaplaybackd")
+										(require-any
+											(_g34 "")
+											(_g36 "")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(_g36 "")
+													(require-all
+														(subpath "/private/var")
+														(require-any
+															(_g36 "")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+														)
+													)
+												)
+											)
+										)
+									)
 								)
 							)
 						)
 					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
 				)
 			)
-			(require-all
-				(extension-class "com.apple.aned.read-only")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.application-group")
-				(_g97 "")
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.application-group")
-				(_g97 "")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(signing-identifier "com.apple.cloudpaird")
 		(require-any
 			(require-all
-				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read")
 				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
+					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
 				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-				(signing-identifier "com.apple.fileindexerd")
+				(signing-identifier "com.apple.chronod")
+			)
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(signing-identifier "com.apple.momentsd")
+		(require-any
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.momentsd")
+				(_g53 "")
 			)
 			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-				(signing-identifier "com.apple.fileindexerd")
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(require-any
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+					(require-all
+						(extension-class "com.apple.app-sandbox.read-write")
+						(signing-identifier "com.apple.momentsd")
+						(_g53 "")
+					)
+				)
 			)
+			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		(signing-identifier "com.apple.fileindexerd")
+	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 										(extension "com.apple.security.exception.files.absolute-path.read-only")
 										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 									)
+									(require-all
+										(extension "com.apple.security.exception.files.absolute-path.read-write")
+										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+									)
 									(require-all
 										(extension "com.apple.security.exception.files.home-relative-path.read-only")
 										(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 									)
 								)
 							)
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-							)
 							(require-any
 								(subpath "/private/var/factory_mount/[^/]+/Applications")
 								(subpath "/private/var/personalized_automation/Applications")

 								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
 							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
 							(subpath "/Applications")
 							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
 							(subpath "/private/var/containers/Bundle")
 						)
 					)

 		(extension-class "com.apple.mediaserverd.read-write")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g91 "")
+			(_g86 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g91 "")
+					(_g86 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g91 "")
+							(_g86 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.sandbox.container")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-any
-					(require-all
-						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-					(require-all
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-				)
+				(extension "com.apple.security.exception.files.absolute-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 			)
 		)
 	)

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g33 "")
+					(_g23 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g33 "")
+							(_g23 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g29 "")
-											(_g31 "")
+											(_g19 "")
+											(_g21 "")
 											(require-all
-												(subpath "/private/var")
 												(require-any
-													(_g31 "")
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(_g21 "")
 													(require-all
+														(subpath "/private/var")
 														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(require-any
-															(_g31 "")
+															(_g21 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 		(extension-class "com.apple.mediaserverd.read-write")
 		(signing-identifier "com.apple.momentsd")
 		(require-any
-			(_g52 "")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(signing-identifier "com.apple.momentsd")
+				(_g50 "")
+			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(require-any
-					(_g52 "")
 					(extension-class "com.apple.mediaserverd.read")
 					(extension-class "com.apple.mediaserverd.read-write")
+					(require-all
+						(extension-class "com.apple.app-sandbox.read-write")
+						(signing-identifier "com.apple.momentsd")
+						(_g50 "")
+					)
 				)
 			)
 			(subpath "${HOME}/Library/com.apple.momentsd")

 		(require-any
 			(_g65 "")
 			(require-all
-				(subpath "/private/var")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
 				(require-any
 					(_g65 "")
 					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
+						(subpath "/private/var")
 						(require-any
 							(_g65 "")
 							(require-all

 			(extension-class "com.apple.mediaserverd.read-write")
 		)
 	)
+	(require-all
+		(subpath "${HOME}/Library/Assets")
+		(require-any
+			(_g110 "")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(extension "com.apple.assets.read")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+					(_g110 "")
+				)
+			)
+		)
+	)
 	(require-all
 		(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		(require-any

 			)
 		)
 	)
+	(require-all
+		(subpath "/private/var/MobileAsset")
+		(extension-class "com.apple.mediaserverd.read")
+		(extension "com.apple.assets.read")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(extension "com.apple.assets.read")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+		)
+	)
 )
 )
 (deny file-issue-extension

 
 (allow file-read*
 	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.videocodecd")
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read*
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.wapic")
+		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
 		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
+			(require-any
+				(literal "/usr/standalone/firmware/apticket.der")
+				(subpath "/private/var/hardware/FactoryData")
+			)
+			(subpath "/private/preboot")
 		)
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.siriknowledged")
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/containers/Data/System/com.apple.geod")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(system-attribute carrier-build internal-build)
+		(signing-identifier "com.apple.audiomxd")
+		(require-any
+			(literal ".caf")
+			(literal ".wav")
+			(literal ".wave")
+		)
+		(require-any
+			(subpath "${FRONT_USER_HOME}/tmp")
+			(subpath "/private/var/tmp")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(vnode-type DIRECTORY)
 		(require-any
 			(require-all
 				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
+					(subpath "${FRONT_USER_HOME}/Library/AddressBook")
+					(subpath "${FRONT_USER_HOME}/Library/Contacts")
+					(subpath "${FRONT_USER_HOME}/Library/Health")
+					(subpath "${FRONT_USER_HOME}/Library/Mail")
+					(subpath "${FRONT_USER_HOME}/Library/NanoMailKit")
+					(subpath "${FRONT_USER_HOME}/Library/NanoPhotos")
+					(subpath "${FRONT_USER_HOME}/Library/Passes")
+					(subpath "${FRONT_USER_HOME}/Library/Recordings")
+					(subpath "${FRONT_USER_HOME}/Library/Reminders")
+					(subpath "${FRONT_USER_HOME}/Library/SMS")
+					(subpath "${FRONT_USER_HOME}/Library/Safari")
+					(subpath "${FRONT_USER_HOME}/Media/Books")
+					(subpath "${FRONT_USER_HOME}/Media/Downloads")
+					(subpath "${FRONT_USER_HOME}/Media/Recordings")
+					(subpath "${FRONT_USER_HOME}/Media/iTunes_Control")
 				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+				(signing-identifier "com.apple.storagedatad")
 			)
 			(require-all
-				(subpath "/private/var/PersonaVolumes")
 				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					(subpath "${FRONT_USER_HOME}/Library/Notes")
+					(subpath "${FRONT_USER_HOME}/Library/Voicemail")
+				)
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}/Library/Logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "${PROCESS_TEMP_DIR}/powerlog")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
 					(require-all
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					)
+					(require-all
+						(subpath "${HOME}")
+						(require-any
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/log")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/tmp/powerlog")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/wireless/Library/Logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(system-attribute developer-mode)
+		(literal "/mach.*")
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/System/Library/Carrier Bundles")
+		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(require-all
+				(subpath "/System/Library/Carrier Bundles")
+				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						(require-any
+							(require-all
+								(subpath "/System/Library/Carrier Bundles")
+								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "/System/Library/Carrier Bundles")
+						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 					)
 				)
 			)

 )
 (allow file-read*
 	(require-all
-		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
 (allow file-read*
 	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
-		)
-		(signing-identifier "com.apple.storagedatad")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/Developer/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
-		)
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/Applications")
-		(require-any
-			(signing-identifier "com.apple.managedappdistributiond")
-			(signing-identifier "com.apple.storekitd")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+				)
+				(require-any
+					(extension "com.apple.librarian.ubiquity-revision")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
 	)
 )
 (allow file-read*

 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
 				)
 			)
 			(require-all

 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
+		(literal "${FRONT_USER_HOME}")
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.mDNSResponderHelper")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+				(require-any
+					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+					(subpath "${HOME}/Library/AddressBook")
+					(subpath "${HOME}/Library/AddressBook/Delegates")
+				)
+			)
+			(subpath "${HOME}/Library/Fonts")
 		)
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.gpsd")
+		(extension "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.audiomxd")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.mediaserverd.read")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
 		)
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.linkd")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.airplayd")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(require-any
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+			(literal "/private/var/db/com.apple.networkextension.tracker-info")
+			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.security.plist")
+			(require-all
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.cameracaptured")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
 	)
 )
 (allow file-read*

 		(signing-identifier "com.apple.MTLAssetUpgraderD")
 	)
 )
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(require-any
+			(extension "com.apple.sandbox.application-group")
+			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.manageddeviced")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 		(signing-identifier "com.apple.mediaplaybackd")
 	)
 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
+		(signing-identifier "com.apple.siriknowledged")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.momentsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(require-any
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(subpath "${HOME}/Library/com.apple.momentsd")
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+				)
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(subpath "${HOME}/Library/com.apple.momentsd")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
 	)
 )
 (allow file-read*

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
+		)
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.wapic")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.mDNSResponderHelper")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(require-any

 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/AppleInternal/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.storagedatad")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/Developer/Applications")
+		(require-any
+			(signing-identifier "com.apple.managedappdistributiond")
+			(signing-identifier "com.apple.storekitd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.videocodecd")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.audiomxd")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
 (allow file-read*
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-			(literal "/private/var/db/com.apple.networkextension.tracker-info")
-			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-			(literal "/private/var/preferences/com.apple.networkd.plist")
-			(literal "/private/var/preferences/com.apple.security.plist")
 			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
 			)
 			(require-all
-				(process-attribute is-apple-signed-executable)
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
-					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
 		)

 )
 (allow file-read*
 	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.airplayd")
+		(uid 0)
+		(vnode-type CHARACTER-DEVICE)
+		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
+		(literal "/dev/bpf*")
 	)
 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/System/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
 	)
 )
 (allow file-read*

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(extension "com.apple.mediaserverd.read")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.audiomxd")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
-		(require-any
-			(require-any
-				(literal "/usr/standalone/firmware/apticket.der")
-				(subpath "/private/var/hardware/FactoryData")
-			)
-			(subpath "/private/preboot")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-				)
-				(require-any
-					(extension "com.apple.librarian.ubiquity-revision")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
-		(literal "${FRONT_USER_HOME}")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/containers/Data/System/com.apple.geod")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(system-attribute developer-mode)
-		(literal "/mach.*")
-		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(require-all
-				(subpath "/System/Library/Carrier Bundles")
-				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-						(require-any
-							(require-all
-								(subpath "/System/Library/Carrier Bundles")
-								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "/System/Library/Carrier Bundles")
-						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-				(extension "com.apple.tcc.kTCCServiceAddressBook")
-				(require-any
-					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/AddressBook/Delegates")
-				)
-			)
-			(subpath "${HOME}/Library/Fonts")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
-				(require-any
-					(subpath "${HOME}/Library/Assets")
-					(subpath "/private/var/MobileAsset")
-				)
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(uid 0)
-		(vnode-type CHARACTER-DEVICE)
-		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
-		(literal "/dev/bpf*")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.audiomxd")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.linkd")
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.cameracaptured")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.storagedatad")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.anomalydetectiond")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
-		(require-any
-			(extension "com.apple.sandbox.application-group")
-			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(vnode-type DIRECTORY)
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/Library/AddressBook")
-					(subpath "${FRONT_USER_HOME}/Library/Contacts")
-					(subpath "${FRONT_USER_HOME}/Library/Health")
-					(subpath "${FRONT_USER_HOME}/Library/Mail")
-					(subpath "${FRONT_USER_HOME}/Library/NanoMailKit")
-					(subpath "${FRONT_USER_HOME}/Library/NanoPhotos")
-					(subpath "${FRONT_USER_HOME}/Library/Passes")
-					(subpath "${FRONT_USER_HOME}/Library/Recordings")
-					(subpath "${FRONT_USER_HOME}/Library/Reminders")
-					(subpath "${FRONT_USER_HOME}/Library/SMS")
-					(subpath "${FRONT_USER_HOME}/Library/Safari")
-					(subpath "${FRONT_USER_HOME}/Media/Books")
-					(subpath "${FRONT_USER_HOME}/Media/Downloads")
-					(subpath "${FRONT_USER_HOME}/Media/Recordings")
-					(subpath "${FRONT_USER_HOME}/Media/iTunes_Control")
-				)
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/Library/Notes")
-					(subpath "${FRONT_USER_HOME}/Library/Voicemail")
-				)
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}/Library/Logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}/powerlog")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-						)
-					)
-					(require-all
-						(subpath "${HOME}")
-						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(require-all
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-										(signing-identifier "com.apple.storagedatad")
-									)
-									(require-all
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-										(signing-identifier "com.apple.storagedatad")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/log")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/tmp/powerlog")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/wireless/Library/Logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(system-attribute carrier-build internal-build)
-		(signing-identifier "com.apple.audiomxd")
-		(require-any
-			(literal ".caf")
-			(literal ".wav")
-			(literal ".wave")
-		)
-		(require-any
-			(subpath "${FRONT_USER_HOME}/tmp")
-			(subpath "/private/var/tmp")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.dmd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.momentsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(require-any
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-						(subpath "${HOME}/Library/com.apple.momentsd")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-				(subpath "${HOME}/Library/com.apple.momentsd")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
-	)
-)
 (deny file-read*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")

 
 (allow file-read-data
 	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.videocodecd")
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
 	)
 )
 (allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.wapic")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.siriknowledged")
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
-		)
-		(signing-identifier "com.apple.storagedatad")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/Developer/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
-		)
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/Applications")
-		(require-any
-			(signing-identifier "com.apple.managedappdistributiond")
-			(signing-identifier "com.apple.storekitd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.mDNSResponderHelper")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(require-all
-				(subpath "/System/Library/Carrier Bundles")
-				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-						(require-any
-							(require-all
-								(subpath "/System/Library/Carrier Bundles")
-								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "/System/Library/Carrier Bundles")
-						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(subpath "/private/var/factory_mount/[^/]+/Applications")
-			(subpath "/private/var/personalized_automation/Applications")
-			(subpath "/private/var/personalized_debug/Applications")
-			(subpath "/private/var/personalized_factory/[^/]+/Applications")
-		)
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(require-any
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-			(literal "/private/var/db/com.apple.networkextension.tracker-info")
-			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-			(literal "/private/var/preferences/com.apple.networkd.plist")
-			(literal "/private/var/preferences/com.apple.security.plist")
-			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
-					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.airplayd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.siriknowledged")
-						(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-						(require-any
-							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-								)
-							)
-						)
-					)
-					(signing-identifier "com.apple.mediaartworkd")
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-						(subpath "${HOME}")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.siriknowledged")
-								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-								(require-any
-									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.mediaartworkd")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.airplayd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?airplayd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.audiomxd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.videocodecd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?videocodecd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(signing-identifier "com.apple.siriknowledged")
-				(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-				(require-any
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-					(require-all
-						(vnode-type DIRECTORY)
-						(require-any
-							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.mediaserverd.read")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.audiomxd")
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
 (allow file-read-data

 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
-		(require-any
-			(require-any
-				(literal "/usr/standalone/firmware/apticket.der")
-				(subpath "/private/var/hardware/FactoryData")
-			)
-			(subpath "/private/preboot")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
-		(literal "${FRONT_USER_HOME}")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-				)
-				(require-any
-					(extension "com.apple.librarian.ubiquity-revision")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/containers/Data/System/com.apple.geod")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-				(extension "com.apple.tcc.kTCCServiceAddressBook")
-				(require-any
-					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/AddressBook/Delegates")
-				)
-			)
-			(subpath "${HOME}/Library/Fonts")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
-				(require-any
-					(subpath "${HOME}/Library/Assets")
-					(subpath "/private/var/MobileAsset")
-				)
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read-data
-	(require-all
-		(uid 0)
-		(vnode-type CHARACTER-DEVICE)
-		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
-		(literal "/dev/bpf*")
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")

 )
 (allow file-read-data
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(extension "com.apple.revisiond.staging")
+		(extension "com.apple.assets.read")
 		(require-any
 			(require-all
-				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
 			)
 			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-					(require-all
-						(extension "com.apple.revisiond.revision")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(system-attribute developer-mode)
-		(literal "/mach.*")
-		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")

 )
 (allow file-read-data
 	(require-all
-		(signing-identifier "com.apple.audiomxd")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
-		(require-any
-			(extension "com.apple.sandbox.application-group")
-			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.cameracaptured")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.dmd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.storagedatad")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.anomalydetectiond")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow file-read-data

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
 (allow file-read-data
 	(require-all
 		(vnode-type DIRECTORY)

 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 								(signing-identifier "com.apple.storagedatad")
 							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
 						)
 					)
 					(require-all

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(system-attribute developer-mode)
+		(literal "/mach.*")
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 		(require-any
 			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
+				(subpath "/System/Library/Carrier Bundles")
+				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 			)
 			(require-all
-				(subpath "${HOME}")
+				(subpath "/private/var")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						(require-any
+							(require-all
+								(subpath "/System/Library/Carrier Bundles")
+								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
 					)
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
+						(subpath "/System/Library/Carrier Bundles")
+						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 					)
 				)
 			)

 )
 (allow file-read-data
 	(require-all
-		(vnode-type SYMLINK)
+		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+				(require-any
+					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+					(subpath "${HOME}/Library/AddressBook")
+					(subpath "${HOME}/Library/AddressBook/Delegates")
+				)
+			)
+			(subpath "${HOME}/Library/Fonts")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-data
+	(require-all
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
-				(extension "com.apple.revisiond.staging")
 				(require-any
 					(require-all
-						(extension "com.apple.revisiond.revision")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
-					(require-all
+						(extension "com.apple.revisiond.staging")
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+						)
 						(require-any
 							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
 							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 							(require-all
-								(extension "com.apple.revisiond.revision")
+								(extension "com.apple.revisiond.staging")
 								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 								)
 								(require-any
 									(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")

 					)
 				)
 			)
+			(require-all
+				(extension "com.apple.revisiond.staging")
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(require-any
+			(require-any
+				(literal "/usr/standalone/firmware/apticket.der")
+				(subpath "/private/var/hardware/FactoryData")
+			)
+			(subpath "/private/preboot")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.mediaserverd.read")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.linkd")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.audiomxd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.airplayd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(require-any
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+			(literal "/private/var/db/com.apple.networkextension.tracker-info")
+			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.security.plist")
+			(require-all
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.cameracaptured")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.siriknowledged")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(require-any
+			(extension "com.apple.sandbox.application-group")
+			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
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
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 )
 (allow file-read-data
 	(require-all
-		(signing-identifier "com.apple.linkd")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-data
+	(require-all
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
 			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.manageddeviced")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+				)
+				(require-any
+					(extension "com.apple.librarian.ubiquity-revision")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.mDNSResponderHelper")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.videocodecd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
+		)
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.wapic")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.storagedatad")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(subpath "/private/var/factory_mount/[^/]+/Applications")
+			(subpath "/private/var/personalized_automation/Applications")
+			(subpath "/private/var/personalized_debug/Applications")
+			(subpath "/private/var/personalized_factory/[^/]+/Applications")
+		)
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/AppleInternal/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.audiomxd")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
+	)
+)
+(allow file-read-data
+	(require-all
+		(vnode-type DIRECTORY SYMLINK)
+		(extension "com.apple.revisiond.revision")
+		(require-any
+			(require-all
+				(extension "com.apple.revisiond.staging")
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+					(require-all
+						(extension "com.apple.revisiond.staging")
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(uid 0)
+		(vnode-type CHARACTER-DEVICE)
+		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
+		(literal "/dev/bpf*")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+		(require-any
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)
 )
 (allow file-read-data
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+	(require-all
+		(subpath "/private/var/containers/Data/System/com.apple.geod")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
+		(literal "${FRONT_USER_HOME}")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/System/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/Developer/Applications")
+		(require-any
+			(signing-identifier "com.apple.managedappdistributiond")
+			(signing-identifier "com.apple.storekitd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.siriknowledged")
+						(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+						(require-any
+							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+								)
+							)
+						)
+					)
+					(signing-identifier "com.apple.mediaartworkd")
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+						(subpath "${HOME}")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.siriknowledged")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(require-any
+									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+									(require-all
+										(vnode-type DIRECTORY)
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.mediaartworkd")
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.airplayd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?airplayd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.audiomxd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.nanophoned")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
+					(require-all
+						(signing-identifier "com.apple.videocodecd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?videocodecd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(signing-identifier "com.apple.siriknowledged")
+				(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+				(require-any
+					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+					(require-all
+						(vnode-type DIRECTORY)
+						(require-any
+							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+						)
+					)
+				)
+			)
+		)
 	)
 )
 (deny file-read-data

 (allow file-read-metadata
 	(with report)
 	(require-all
-		(literal "${HOME}")
-		(signing-identifier "com.apple.siri.context.service")
+		(literal "${HOME}/Library/Preferences")
+		(signing-identifier "com.apple.installcoordinationd")
 	)
 )
 (allow file-read-metadata
 	(with report)
 	(require-all
-		(literal "${HOME}/Library/Preferences")
+		(literal "${HOME}")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.network.client")
 			(%entitlement-is-bool-true "com.apple.security.ts.addressbook")

 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Logs")
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Logs")
-		(signing-identifier "com.apple.storagedatad")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
 	)
 )
 (allow file-read-metadata

 		(literal "${FRONT_USER_HOME}")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 			(require-all
 				(vnode-type DIRECTORY)
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
 				(require-any
-					(extension "com.apple.revisiond.staging")
+					(extension "com.apple.revisiond.revision")
 					(require-all
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
-						(extension "com.apple.revisiond.revision")
+						(extension "com.apple.revisiond.staging")
 					)
 				)
 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)
-						(extension "com.apple.revisiond.revision")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
-				(require-any
-					(require-all
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(extension "com.apple.revisiond.revision")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+								)
+								(extension "com.apple.revisiond.staging")
+							)
 						)
-						(extension "com.apple.revisiond.revision")
 					)
 					(require-all
 						(require-any

 							(subpath "/private/var/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
+			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
+				(require-any
+					(extension "com.apple.revisiond.revision")
+					(require-all
 						(require-any
-							(extension "com.apple.revisiond.staging")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-								)
-								(extension "com.apple.revisiond.revision")
-							)
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(extension "com.apple.revisiond.staging")
 					)
 				)
 			)

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
-		)
+		(signing-identifier "com.apple.internal.livtipsd")
+		(literal "${HOME}/Library/PPTDevice")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read-metadata

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Notes")
+			(subpath "${FRONT_USER_HOME}/Library/Voicemail")
+		)
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(require-any

 		(signing-identifier "com.apple.storagedatad")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Notes")
-			(subpath "${FRONT_USER_HOME}/Library/Voicemail")
-		)
-		(signing-identifier "com.apple.storagedatad")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "${PROCESS_TEMP_DIR}/powerlog")

 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 						(signing-identifier "com.apple.storagedatad")
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+						)
+					)
 				)
 			)
 			(require-all

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/Developer/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
+		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.internal.livtipsd")
-		(literal "${HOME}/Library/PPTDevice")
+		(subpath "/System/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read-metadata

 		(signing-identifier "com.apple.fileindexerd")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(literal "${HOME}/Library/PPTDevice")
-		(require-any
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")

 )
 (allow file-read-metadata
 	(require-all
-		(literal "${HOME}/Library/Preferences")
+		(literal "${HOME}/Library/PPTDevice")
+		(require-any
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "${HOME}")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.network.client")
 			(%entitlement-is-bool-true "com.apple.security.ts.addressbook")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var/containers/Bundle")
+		(require-any
+			(subpath "/private/var/factory_mount/[^/]+/Applications")
+			(subpath "/private/var/personalized_automation/Applications")
+			(subpath "/private/var/personalized_debug/Applications")
+			(subpath "/private/var/personalized_factory/[^/]+/Applications")
+		)
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
-		)
+		(subpath "/AppleInternal/Applications")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
 		)
 	)
 )

 	(require-all
 		(signing-identifier "com.apple.linkd")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/Applications")
+		(subpath "/Developer/Applications")
 		(require-any
 			(signing-identifier "com.apple.managedappdistributiond")
 			(signing-identifier "com.apple.storekitd")

 		(require-any
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
 			)
 		)

 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 		(signing-identifier "com.apple.mediaplaybackd")
 	)

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.dmd")
+		(signing-identifier "com.apple.manageddeviced")
 		(require-any
 			(require-all
 				(subpath "/private/var")

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.gpsd")
+		(signing-identifier "com.apple.announced")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.announced")
+		(signing-identifier "com.apple.gpsd")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
 		)
 	)
 )

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)

 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
 		)
 	)
 )

 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
 				)
 			)
 			(require-all

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
 					(subpath "${HOME}/Library/Assets")
 					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
 		)
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type DIRECTORY SYMLINK)
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
 			(require-all

 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)

 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow file-read-metadata
 	(require-all
-		(require-any
-			(subpath "/private/var/factory_mount/[^/]+/Applications")
-			(subpath "/private/var/personalized_automation/Applications")
-			(subpath "/private/var/personalized_debug/Applications")
-			(subpath "/private/var/personalized_factory/[^/]+/Applications")
-		)
+		(subpath "/private/var/containers/Bundle")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)

 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 								(signing-identifier "com.apple.storagedatad")
 							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
 						)
 					)
 					(require-all

 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 							(require-all
 								(require-any
 									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 								)

 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)

 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)

 	)
 )
 
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
+		)
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.videocodecd")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.wapic")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.mDNSResponderHelper")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/AppleInternal/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/System/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var/containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(subpath "/private/var/factory_mount/[^/]+/Applications")
+			(subpath "/private/var/personalized_automation/Applications")
+			(subpath "/private/var/personalized_debug/Applications")
+			(subpath "/private/var/personalized_factory/[^/]+/Applications")
+		)
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.audiomxd")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.mediaplaybackd")
+				(signing-identifier "com.apple.videocodecd")
+			)
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.mediaserverd.read")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.airplayd")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(require-any
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+			(literal "/private/var/db/com.apple.networkextension.tracker-info")
+			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.security.plist")
+			(require-all
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.siriknowledged")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
+		(literal "${FRONT_USER_HOME}")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+				)
+				(require-any
+					(extension "com.apple.librarian.ubiquity-revision")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(require-any
+			(require-any
+				(literal "/usr/standalone/firmware/apticket.der")
+				(subpath "/private/var/hardware/FactoryData")
+			)
+			(subpath "/private/preboot")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/System/Library/Carrier Bundles")
+		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(require-all
+				(subpath "/System/Library/Carrier Bundles")
+				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						(require-any
+							(require-all
+								(subpath "/System/Library/Carrier Bundles")
+								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "/System/Library/Carrier Bundles")
+						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+		)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(extension "com.apple.assets.read")
 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
 					(subpath "${HOME}/Library/Assets")
 					(subpath "/private/var/MobileAsset")
 				)
 			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(vnode-type DIRECTORY SYMLINK)
+		(extension "com.apple.revisiond.revision")
+		(require-any
 			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
+				(extension "com.apple.revisiond.staging")
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+					(require-all
+						(extension "com.apple.revisiond.staging")
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+						)
+					)
+				)
 			)
 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+				(require-any
+					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+					(subpath "${HOME}/Library/AddressBook")
+					(subpath "${HOME}/Library/AddressBook/Delegates")
+				)
+			)
+			(subpath "${HOME}/Library/Fonts")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var/containers/Data/System/com.apple.geod")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(subpath "/AppleInternal")

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
 	)
 )
 (allow file-read-xattr

 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(uid 0)
+		(vnode-type CHARACTER-DEVICE)
+		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
+		(literal "/dev/bpf*")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.audiomxd")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.momentsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(require-any
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(subpath "${HOME}/Library/com.apple.momentsd")
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+				)
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(subpath "${HOME}/Library/com.apple.momentsd")
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.cameracaptured")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/Developer/Applications")
+		(require-any
+			(signing-identifier "com.apple.managedappdistributiond")
+			(signing-identifier "com.apple.storekitd")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.storagedatad")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(require-any
+			(extension "com.apple.sandbox.application-group")
+			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.manageddeviced")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.siriknowledged")
+						(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+						(require-any
+							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+								)
+							)
+						)
+					)
+					(signing-identifier "com.apple.mediaartworkd")
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+						(subpath "${HOME}")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.siriknowledged")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(require-any
+									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+									(require-all
+										(vnode-type DIRECTORY)
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.mediaartworkd")
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.airplayd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?airplayd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.audiomxd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.nanophoned")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
+					(require-all
+						(signing-identifier "com.apple.videocodecd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?videocodecd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(signing-identifier "com.apple.siriknowledged")
+				(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+				(require-any
+					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+					(require-all
+						(vnode-type DIRECTORY)
+						(require-any
+							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.linkd")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(system-attribute carrier-build internal-build)

 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(vnode-type DIRECTORY)

 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 								(signing-identifier "com.apple.storagedatad")
 							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
 						)
 					)
 					(require-all

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
-		(require-any
-			(require-any
-				(literal "/usr/standalone/firmware/apticket.der")
-				(subpath "/private/var/hardware/FactoryData")
-			)
-			(subpath "/private/preboot")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
-				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-				(extension "com.apple.tcc.kTCCServiceAddressBook")
-				(require-any
-					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/AddressBook/Delegates")
-				)
-			)
-			(subpath "${HOME}/Library/Fonts")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(require-all
-				(subpath "/System/Library/Carrier Bundles")
-				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-			)
-			(require-all
-				(subpath "/private/var")
+				(extension "com.apple.revisiond.revision")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						(extension "com.apple.revisiond.staging")
 						(require-any
-							(require-all
-								(subpath "/System/Library/Carrier Bundles")
-								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-							)
-							(subpath "${FRONT_USER_HOME}")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 						)
 					)
 					(require-all
-						(subpath "/System/Library/Carrier Bundles")
-						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(require-any
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-			(literal "/private/var/db/com.apple.networkextension.tracker-info")
-			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-			(literal "/private/var/preferences/com.apple.networkd.plist")
-			(literal "/private/var/preferences/com.apple.security.plist")
-			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
-					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-							(subpath "${FRONT_USER_HOME}")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(extension "com.apple.revisiond.staging")
+								(require-any
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+								)
+								(require-any
+									(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+									(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+								)
 							)
 						)
 					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					)
 				)
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.airplayd")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.mediaserverd.read")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
+			(require-all
+				(extension "com.apple.revisiond.staging")
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
 		)
 	)
 )

 		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.linkd")
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.audiomxd")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.momentsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(require-any
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-						(subpath "${HOME}/Library/com.apple.momentsd")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-				(subpath "${HOME}/Library/com.apple.momentsd")
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.siriknowledged")
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.dmd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.cameracaptured")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.anomalydetectiond")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-				)
-				(require-any
-					(extension "com.apple.librarian.ubiquity-revision")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
-		)
-		(signing-identifier "com.apple.storagedatad")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.mDNSResponderHelper")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
-		(require-any
-			(extension "com.apple.sandbox.application-group")
-			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.storagedatad")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
-		)
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.siriknowledged")
-						(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-						(require-any
-							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-								)
-							)
-						)
-					)
-					(signing-identifier "com.apple.mediaartworkd")
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-						(subpath "${HOME}")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.siriknowledged")
-								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-								(require-any
-									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.mediaartworkd")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.airplayd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?airplayd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.audiomxd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.videocodecd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?videocodecd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(signing-identifier "com.apple.siriknowledged")
-				(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-				(require-any
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-					(require-all
-						(vnode-type DIRECTORY)
-						(require-any
-							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.wapic")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.videocodecd")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/Developer/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.audiomxd")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(vnode-type SYMLINK)
-		(require-any
-			(require-all
-				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
-				(extension "com.apple.revisiond.staging")
-				(require-any
-					(require-all
-						(extension "com.apple.revisiond.revision")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-							(require-all
-								(extension "com.apple.revisiond.revision")
-								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-								)
-								(require-any
-									(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-									(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-								)
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
-		(literal "${FRONT_USER_HOME}")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(extension "com.apple.revisiond.staging")
-		(require-any
-			(require-all
-				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-					(require-all
-						(extension "com.apple.revisiond.revision")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(uid 0)
-		(vnode-type CHARACTER-DEVICE)
-		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
-		(literal "/dev/bpf*")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var/containers/Data/System/com.apple.geod")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var/containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(subpath "/private/var/factory_mount/[^/]+/Applications")
-			(subpath "/private/var/personalized_automation/Applications")
-			(subpath "/private/var/personalized_debug/Applications")
-			(subpath "/private/var/personalized_factory/[^/]+/Applications")
-		)
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/Applications")
-		(require-any
-			(signing-identifier "com.apple.managedappdistributiond")
-			(signing-identifier "com.apple.storekitd")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.mediaplaybackd")
-				(signing-identifier "com.apple.videocodecd")
-			)
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-		)
-	)
-)
 (deny file-read-xattr
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")

 
 (allow file-write*
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-write*
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-write*
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+		)
+	)
+)
+(allow file-write*
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-write*
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
 	)
 )
 (allow file-write*

 )
 (allow file-write*
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-	)
-)
-(allow file-write*
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
 	)
 )
 (allow file-write*
 	(require-all
-		(signing-identifier "com.apple.announced")
+		(subpath "/private/var")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
+			(require-all
+				(signing-identifier "com.apple.manageddeviced")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.manageddeviced")
+								(subpath "/private/var")
+								(extension "com.apple.sandbox.container")
+								(require-any
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											)
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.MTLAssetUpgraderD")
+						)
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-write*
+	(require-all
+		(subpath "/private/var")
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write*
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write*
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-write*
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-write*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+		)
+	)
+)
+(allow file-write*
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-write*
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-write*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
 		)
 	)
 )

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 		)
 	)
 )
-(allow file-write*
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write*
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.dmd")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.dmd")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write*
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-write*
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-write*
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
-		)
-	)
-)
-(allow file-write*
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-write*
-	(require-all
-		(subpath "/private/var")
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-write*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-write*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-		(require-any
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/AddressBook")
-			)
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-write*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-			(require-all
-				(vnode-type SYMLINK)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-		)
-	)
-)
 (allow file-write*
 	(require-all
 		(extension "com.apple.sandbox.container")

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 	)
 )
 (allow file-write*
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
 (allow file-write*

 		(require-any
 			(extension "com.apple.mediaserverd.read-write")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")

 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
 )
 (allow file-write*
 	(require-all
-		(signing-identifier "com.apple.tursd")
+		(signing-identifier "com.apple.nanophoned")
 		(require-any
 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
 		)
 	)

 )
 (allow file-write*
 	(require-all
-		(signing-identifier "com.apple.tursd")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
 		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
 	)
 )
 (deny file-write*

 
 (allow file-write-create
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-write-create
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(subpath "/private/var")
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+	)
+)
+(allow file-write-create
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.manageddeviced")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.manageddeviced")
+								(subpath "/private/var")
+								(extension "com.apple.sandbox.container")
+								(require-any
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											)
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.MTLAssetUpgraderD")
+						)
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
 	)
 )
 (allow file-write-create

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 		)
 	)
 )
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-	)
-)
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
 (allow file-write-create
 	(require-all
 		(subpath "/private/var")

 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
 				)
 			)
 			(require-all

 		)
 	)
 )
+(allow file-write-create
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
 (allow file-write-create
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-write-create
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
 (allow file-write-create
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")

 )
 (allow file-write-create
 	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.dmd")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.dmd")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(subpath "/private/var")
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write-create
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
 			(require-all

 		)
 	)
 )
+(allow file-write-create
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(literal "${FRONT_USER_HOME}/tmp/AudioCapture")
+		(vnode-type SYMLINK)
+		(require-any
+			(require-all
+				(system-attribute carrier-build)
+				(signing-identifier "com.apple.audiomxd")
+			)
+			(require-all
+				(system-attribute internal-build)
+				(signing-identifier "com.apple.audiomxd")
+			)
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
 (allow file-write-create
 	(require-all
 		(%entitlement-is-present "com.apple.security.ts.tmpdir")

 		)
 	)
 )
-(allow file-write-create
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
 (allow file-write-create
 	(require-all
 		(vnode-type REGULAR-FILE)

 		)
 	)
 )
-(allow file-write-create
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
 (allow file-write-create
 	(require-all
 		(require-any

 		(signing-identifier "com.apple.chronod")
 	)
 )
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
 (allow file-write-create
 	(require-all
 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(require-any
 			(extension "com.apple.mediaserverd.read-write")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
 		)
 	)
 )
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
 (allow file-write-create
 	(require-all
 		(signing-identifier "com.apple.momentsd")
 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
 )
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-		)
-	)
-)
 (allow file-write-create
 	(require-all
 		(vnode-type DIRECTORY)

 													)
 													(require-all
 														(subpath "${FRONT_USER_HOME}")
-														(signing-identifier "com.apple.nanophoned")
+														(signing-identifier "com.apple.tursd")
 														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 													)
 												)

 									)
 									(require-all
 										(signing-identifier "com.apple.nanophoned")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-									)
-									(require-all
-										(signing-identifier "com.apple.tursd")
 										(require-any
 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 											(require-all

 											)
 										)
 									)
+									(require-all
+										(signing-identifier "com.apple.tursd")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+									)
 								)
 							)
 						)

 			)
 			(require-all
 				(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs")
-				(signing-identifier "com.apple.nanophoned")
+				(signing-identifier "com.apple.tursd")
 			)
 			(require-all
 				(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync")
-				(signing-identifier "com.apple.nanophoned")
+				(signing-identifier "com.apple.tursd")
 			)
 			(require-all
 				(literal "${HOME}/Library/Caches")

 											)
 											(require-all
 												(subpath "${FRONT_USER_HOME}")
-												(signing-identifier "com.apple.nanophoned")
+												(signing-identifier "com.apple.tursd")
 												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 											)
 										)

 							)
 							(require-all
 								(signing-identifier "com.apple.nanophoned")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-							)
-							(require-all
-								(signing-identifier "com.apple.tursd")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
 									(require-all

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.tursd")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+							)
 						)
 					)
 				)

 )
 (allow file-write-create
 	(require-all
-		(literal "/private/var/tmp/AudioCapture")
-		(vnode-type SYMLINK)
-		(require-any
-			(require-all
-				(system-attribute carrier-build)
-				(signing-identifier "com.apple.audiomxd")
-			)
-			(require-all
-				(system-attribute internal-build)
-				(signing-identifier "com.apple.audiomxd")
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(require-any
-					(require-any
-						(signing-identifier "com.apple.internal.livtipsd")
-						(signing-identifier "com.apple.usernotificationsd")
-					)
-					(signing-identifier "com.apple.Carousel")
-					(signing-identifier "com.apple.FTLivePhotoService")
-					(signing-identifier "com.apple.announced")
-					(signing-identifier "com.apple.asktod")
-					(signing-identifier "com.apple.facetimemessagestored")
-				)
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.asktod")
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(signing-identifier "com.apple.tursd")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
 		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
 	)
 )
 (allow file-write-create

 		)
 	)
 )
+(allow file-write-create
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+		)
+	)
+)
 (allow file-write-create
 	(require-all
 		(require-any
-			(literal "${FRONT_USER_HOME}/tmp/AudioCapture")
 			(literal "${PROCESS_TEMP_DIR}/AudioCapture")
+			(literal "/private/var/tmp/AudioCapture")
 		)
 		(vnode-type SYMLINK)
 		(require-any

 		)
 	)
 )
+(allow file-write-create
+	(require-all
+		(vnode-type REGULAR-FILE)
+		(require-any
+			(require-all
+				(subpath "${PROCESS_TEMP_DIR}")
+				(signing-identifier "com.apple.FTLivePhotoService")
+			)
+			(require-all
+				(subpath "/private/var/tmp")
+				(require-any
+					(require-any
+						(signing-identifier "com.apple.internal.livtipsd")
+						(signing-identifier "com.apple.usernotificationsd")
+					)
+					(signing-identifier "com.apple.Carousel")
+					(signing-identifier "com.apple.FTLivePhotoService")
+					(signing-identifier "com.apple.announced")
+					(signing-identifier "com.apple.asktod")
+					(signing-identifier "com.apple.facetimemessagestored")
+				)
+			)
+		)
+	)
+)
 (deny file-write-create
 	(with no-report)
 	(require-all

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+					)
+				)
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
-					)
-				)
+				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 			)
 		)
 	)

 	)
 )
 
-(allow file-write-data
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
 (allow file-write-data
 	(require-all
 		(signing-identifier "com.apple.privacyaccountingctl")

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 )
 (allow file-write-data
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(vnode-type DIRECTORY)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(require-any
+							(extension "com.apple.revisiond.staging")
+							(require-all
+								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
+		)
 	)
 )
 (allow file-write-data

 		)
 	)
 )
-(allow file-write-data
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-write-data
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-write-data
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
-	)
-)
 (allow file-write-data
 	(require-all
 		(signing-identifier "com.apple.announced")

 		)
 	)
 )
-(allow file-write-data
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
-	)
-)
 (allow file-write-data
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 	)
 )
 (allow file-write-data

 		(subpath "${FRONT_USER_HOME}/Library/Keychains")
 	)
 )
+(allow file-write-data
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-data
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
+	)
+)
 (allow file-write-data
 	(require-all
 		(subpath "/private/var")
 		(require-any
 			(require-all
-				(signing-identifier "com.apple.dmd")
+				(signing-identifier "com.apple.manageddeviced")
 				(subpath "/private/var")
 				(extension "com.apple.sandbox.container")
 				(require-any

 				(require-any
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
 						(require-any
 							(require-all
-								(signing-identifier "com.apple.dmd")
+								(signing-identifier "com.apple.manageddeviced")
 								(subpath "/private/var")
 								(extension "com.apple.sandbox.container")
 								(require-any

 						)
 					)
 					(require-all
-						(signing-identifier "com.apple.dmd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
 						(subpath "/private/var")
 						(extension "com.apple.sandbox.container")
 						(require-any

 					)
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
 								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")

 										)
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
 									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
 								)
 							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
 						)
 					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
 				)
 			)
 		)

 (allow file-write-data
 	(require-all
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-write-data
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-write-data
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
+	)
+)
+(allow file-write-data
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+	)
+)
+(allow file-write-data
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 		)
-		(signing-identifier "com.apple.chronod")
 	)
 )
 (allow file-write-data

 )
 (allow file-write-data
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
 			(require-all

 		)
 	)
 )
-(allow file-write-data
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-write-data
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-write-data
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
 (allow file-write-data
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")

 )
 (allow file-write-data
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-write-data
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+		)
+	)
+)
+(allow file-write-data
+	(require-all
+		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
 			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-write-data
+	(require-all
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
 			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
+				(subpath "${FRONT_USER_HOME}")
 				(require-any
 					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
-				(require-any
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
 					)
 					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-						)
-						(require-any
-							(extension "com.apple.revisiond.staging")
 							(require-all
-								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
 							)
 						)
 					)
 				)
 			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
 		)
 	)
 )
 (allow file-write-data
 	(require-all
-		(extension "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.geoanalyticsd")
 		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-write-data
+	(require-all
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 		)
 	)
 )

 		(require-any
 			(extension "com.apple.mediaserverd.read-write")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 		)
 	)
 )
-(allow file-write-data
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
-(allow file-write-data
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
 (allow file-write-data
 	(require-all
 		(signing-identifier "com.apple.anomalydetectiond")
 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
 )
 (allow file-write-data
 	(require-all
-		(signing-identifier "com.apple.tursd")
+		(signing-identifier "com.apple.nanophoned")
 		(require-any
 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
-		)
-	)
-)
-(allow file-write-data
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
 		)
 	)
 )

 
 (allow file-write-mode
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-write-mode
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
 	)
 )
 (allow file-write-mode

 )
 (allow file-write-mode
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-	)
-)
-(allow file-write-mode
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
 	)
 )
 (allow file-write-mode
 	(require-all
-		(signing-identifier "com.apple.announced")
+		(subpath "/private/var")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
+			(require-all
+				(signing-identifier "com.apple.manageddeviced")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.manageddeviced")
+								(subpath "/private/var")
+								(extension "com.apple.sandbox.container")
+								(require-any
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											)
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.MTLAssetUpgraderD")
+						)
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(subpath "/private/var")
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-write-mode
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-write-mode
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
 		)
 	)
 )

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 		)
 	)
 )
-(allow file-write-mode
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write-mode
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.dmd")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.dmd")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write-mode
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-write-mode
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-write-mode
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
-		)
-	)
-)
-(allow file-write-mode
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-write-mode
-	(require-all
-		(subpath "/private/var")
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write-mode
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-write-mode
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-write-mode
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-		(require-any
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/AddressBook")
-			)
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-write-mode
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-			(require-all
-				(vnode-type SYMLINK)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-		)
-	)
-)
 (allow file-write-mode
 	(require-all
 		(extension "com.apple.sandbox.container")

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 	)
 )
 (allow file-write-mode
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
 (allow file-write-mode

 		(require-any
 			(extension "com.apple.mediaserverd.read-write")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")

 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
 )
 (allow file-write-mode
 	(require-all
-		(signing-identifier "com.apple.tursd")
+		(signing-identifier "com.apple.nanophoned")
 		(require-any
 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
 		)
 	)

 )
 (allow file-write-mode
 	(require-all
-		(signing-identifier "com.apple.tursd")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
 		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
 	)
 )
 (deny file-write-mode

 
 (allow file-write-owner
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-write-owner
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
 	)
 )
 (allow file-write-owner

 )
 (allow file-write-owner
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-	)
-)
-(allow file-write-owner
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
 	)
 )
 (allow file-write-owner
 	(require-all
-		(signing-identifier "com.apple.announced")
+		(subpath "/private/var")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
+			(require-all
+				(signing-identifier "com.apple.manageddeviced")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.manageddeviced")
+								(subpath "/private/var")
+								(extension "com.apple.sandbox.container")
+								(require-any
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											)
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.MTLAssetUpgraderD")
+						)
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(subpath "/private/var")
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-write-owner
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-write-owner
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
 		)
 	)
 )

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 		)
 	)
 )
-(allow file-write-owner
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write-owner
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.dmd")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.dmd")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write-owner
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-write-owner
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-write-owner
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
-		)
-	)
-)
-(allow file-write-owner
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-write-owner
-	(require-all
-		(subpath "/private/var")
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write-owner
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-write-owner
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-write-owner
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-		(require-any
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/AddressBook")
-			)
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-write-owner
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-			(require-all
-				(vnode-type SYMLINK)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(extension "com.apple.revisiond.staging")
-			)
-		)
-	)
-)
 (allow file-write-owner
 	(require-all
 		(extension "com.apple.sandbox.container")

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 	)
 )
 (allow file-write-owner
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
 (allow file-write-owner

 		(require-any
 			(extension "com.apple.mediaserverd.read-write")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")

 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)
 )
 (allow file-write-owner
 	(require-all
-		(signing-identifier "com.apple.tursd")
+		(signing-identifier "com.apple.nanophoned")
 		(require-any
 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
 		)
 	)

 )
 (allow file-write-owner
 	(require-all
-		(signing-identifier "com.apple.tursd")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
 		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
 	)
 )
 (deny file-write-owner

 
 (deny file-write-setugid)
 
-(allow file-write-unlink
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")

 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
 						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
 				)
 			)
 			(require-all

 		)
 	)
 )
+(allow file-write-unlink
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.manageddeviced")
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.manageddeviced")
+								(subpath "/private/var")
+								(extension "com.apple.sandbox.container")
+								(require-any
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											)
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.MTLAssetUpgraderD")
+						)
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
 (allow file-write-unlink
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(signing-identifier "com.apple.momentsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(require-any
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(subpath "${HOME}/Library/com.apple.momentsd")
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+				)
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(subpath "${HOME}/Library/com.apple.momentsd")
+			)
+		)
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
+	)
+)
+(allow file-write-unlink
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+	)
+)
+(allow file-write-unlink
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
 	)
 )
 (allow file-write-unlink

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 )
 (allow file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+			)
+			(subpath "${HOME}/Library/AddressBook/Delegates")
+		)
 	)
 )
 (allow file-write-unlink

 )
 (allow file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(subpath "/private/var")
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.chronod")
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-write-unlink

 		)
 	)
 )
-(allow file-write-unlink
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-		(require-any
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/AddressBook")
-			)
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(signing-identifier "com.apple.momentsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(require-any
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-						(subpath "${HOME}/Library/com.apple.momentsd")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-				(subpath "${HOME}/Library/com.apple.momentsd")
-			)
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
-		)
-	)
-)
 (allow file-write-unlink
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 		)
 	)
 )
-(allow file-write-unlink
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
-	)
-)
 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
 		(require-any
-			(require-all
-				(signing-identifier "com.apple.dmd")
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.dmd")
-						(subpath "/private/var")
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
-						)
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
 		)
+		(signing-identifier "com.apple.chronod")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
 		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
 		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
 	)
 )
 (allow file-write-unlink

 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 )
 (allow file-write-unlink
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
 		(require-any
-			(extension "com.apple.mediaserverd.read-write")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
 		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 	)
 )
 (allow file-write-unlink

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)
 )
+(allow file-write-unlink
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+		)
+	)
+)
 (allow file-write-unlink
 	(require-all
 		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(subpath "${PROCESS_TEMP_DIR}")
+				(signing-identifier "com.apple.FTLivePhotoService")
+			)
+			(require-all
+				(subpath "/private/var/tmp")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 					(require-any

 					(signing-identifier "com.apple.facetimemessagestored")
 				)
 			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.asktod")
-			)
 		)
 	)
 )

 		(signing-identifier "com.apple.chronod")
 	)
 )
-(allow file-write-xattr
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-	)
-)
 (allow file-write-xattr
 	(require-all
 		(signing-identifier "com.apple.privacyaccountingctl")

 )
 (allow file-write-xattr
 	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+		)
 	)
 )
 (allow file-write-xattr
 	(require-all
-		(signing-identifier "com.apple.gpsd")
+		(signing-identifier "com.apple.announced")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
 		)
 	)
 )

 		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 	)
 )
-(allow file-write-xattr
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
 (allow file-write-xattr
 	(require-all
 		(xattr "com.apple.metadata:com_apple_backup_excludeItem")

 				(subpath "${FRONT_USER_HOME}")
 				(require-any
 					(require-all
-						(signing-identifier "com.apple.audiomxd")
+						(signing-identifier "com.apple.mediaplaybackd")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
 								(subpath "${HOME}")

 		)
 	)
 )
+(allow file-write-xattr
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+			(signing-identifier "com.apple.cameracaptured")
+		)
+	)
+)
 (allow file-write-xattr
 	(require-all
 		(require-any

 )
 (allow file-write-xattr
 	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(signing-identifier "com.apple.gpsd")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
 		)
 	)
 )

 )
 (allow file-write-xattr
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
 			(require-all

 		)
 	)
 )
+(allow file-write-xattr
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
 (allow file-write-xattr
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 )
 (allow file-write-xattr
 	(require-all
-		(extension "com.apple.mediaserverd.read-write")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
 		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-			(signing-identifier "com.apple.cameracaptured")
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
 		)
 	)
 )

 		(signing-identifier "com.apple.fileindexerd")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
 		)
 	)

 		(require-any
 			(extension "com.apple.mediaserverd.read-write")
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 				(subpath "${HOME}/Library/com.apple.momentsd")

 )
 (allow file-write-xattr
 	(require-all
-		(signing-identifier "com.apple.tursd")
+		(signing-identifier "com.apple.nanophoned")
 		(require-any
 			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
 			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
 				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
 			)
 		)
 	)

 		(require-any
 			(require-all
 				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
 				)
 			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
 			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 		)
 	)

 		(subpath "/private/var")
 		(require-any
 			(require-all
-				(signing-identifier "com.apple.dmd")
+				(signing-identifier "com.apple.manageddeviced")
 				(subpath "/private/var")
 				(extension "com.apple.sandbox.container")
 				(require-any

 				(require-any
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
 						(require-any
 							(require-all
-								(signing-identifier "com.apple.dmd")
+								(signing-identifier "com.apple.manageddeviced")
 								(subpath "/private/var")
 								(extension "com.apple.sandbox.container")
 								(require-any

 						)
 					)
 					(require-all
-						(signing-identifier "com.apple.dmd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
 						(subpath "/private/var")
 						(extension "com.apple.sandbox.container")
 						(require-any

 					)
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(signing-identifier "com.apple.manageddeviced")
+						(subpath "/private/var")
+						(extension "com.apple.sandbox.container")
 						(require-any
 							(require-all
-								(signing-identifier "com.apple.dmd")
-								(subpath "/private/var")
-								(extension "com.apple.sandbox.container")
 								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")

 										)
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
 									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											)
-										)
-									)
 								)
 							)
-							(signing-identifier "com.apple.MTLAssetUpgraderD")
 						)
 					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
 				)
 			)
 		)

 )
 (allow file-write-xattr
 	(require-all
-		(signing-identifier "com.apple.tursd")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
 			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
 		)
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
 	)
 )
 (allow file-write-xattr

 					)
 					(require-all
 						(signing-identifier "com.apple.nanophoned")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
 							(require-all

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
 					(require-all
 						(signing-identifier "com.apple.videocodecd")
 						(require-any

 (allow iokit-open-user-client
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.network.client")
+			(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
+		)
+	)
+)
 (allow iokit-open-user-client
 	(require-all
 		(require-any

 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-open-user-client
-	(require-all
-		(iokit-registry-entry-class "AppleKeyStoreUserClient")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.network.client")
-			(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
-		)
-	)
-)
 (allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "IOMobileFramebufferUserClient")
 		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		)
 	)
 )
 (allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(iokit-registry-entry-class "AGXDevice")
+			(iokit-registry-entry-class "AppleJPEGDriverUserClient")
+			(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
+			(iokit-registry-entry-class "IOSurfaceRootUserClient")
+		)
+	)
+)
+(allow iokit-open-user-client
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		(require-any
 			(iokit-registry-entry-class "AGXDevice")
 			(iokit-registry-entry-class "AppleJPEGDriverUserClient")

 		)
 	)
 )
-(allow iokit-open-user-client
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(require-any
-			(iokit-registry-entry-class "AGXDevice")
-			(iokit-registry-entry-class "AppleJPEGDriverUserClient")
-			(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
-			(iokit-registry-entry-class "IOSurfaceRootUserClient")
-		)
-	)
-)
 (allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")

 			(iokit-registry-entry-class "AGXCommandQueue")
 			(iokit-registry-entry-class "AGXDevice")
 			(iokit-registry-entry-class "AGXSharedUserClient")
+			(iokit-registry-entry-class "IOAccelContext2")
 			(iokit-registry-entry-class "IOGPUDeviceUserClient")
 			(require-any
 				(iokit-connection "IOGPU")

 			)
 			(require-any
 				(iokit-registry-entry-class "IOAccelContext")
-				(iokit-registry-entry-class "IOAccelContext2")
 				(iokit-registry-entry-class "IOAccelDevice")
 				(iokit-registry-entry-class "IOAccelDevice2")
 				(iokit-registry-entry-class "IOAccelSharedUserClient")

 (allow iokit-open-user-client
 	(require-all
 		(system-attribute virtual-device)
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any
 			(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
 			(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")

 		(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
 		(require-any
 			(iokit-registry-entry-class "AGXAcceleratorG*")
-			(iokit-registry-entry-class "AppleParavirtGPU*")
 			(require-any
 				(iokit-registry-entry-class "AppleCLCD*")
 				(iokit-registry-entry-class "AppleParavirtDisplay*")
+				(iokit-registry-entry-class "AppleParavirtGPU*")
 			)
 		)
 	)

 		(require-any
 			(iokit-registry-entry-class "AGXAcceleratorG*")
 			(iokit-registry-entry-class "AppleJPEGDriver")
-			(iokit-registry-entry-class "AppleParavirtGPU*")
 			(iokit-registry-entry-class "IOSurfaceRoot")
 			(require-any
 				(iokit-registry-entry-class "AppleCLCD*")
 				(iokit-registry-entry-class "AppleParavirtDisplay*")
+				(iokit-registry-entry-class "AppleParavirtGPU*")
 			)
 		)
 	)

 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow iokit-open-service
-	(require-all
-		(iokit-registry-entry-class "AppleParavirtGPU*")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
 (allow iokit-open-service
 	(require-all
 		(require-any
 			(iokit-registry-entry-class "AppleCLCD*")
 			(iokit-registry-entry-class "AppleParavirtDisplay*")
+			(iokit-registry-entry-class "AppleParavirtGPU*")
 		)
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.FileCoordination")
+		(global-name "com.apple.awdd")
 		(signing-identifier "com.apple.tursd")
 	)
 )

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.itunescloudd.xpc")
-		(signing-identifier "com.apple.siriknowledged")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.locationd.spi")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.medialibraryd.xpc")
+		(global-name "com.apple.marco")
+		(signing-identifier "com.apple.Carousel")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.itunescloudd.xpc")
 		(signing-identifier "com.apple.siriknowledged")
 	)
 )

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.marco")
-		(signing-identifier "com.apple.asktod")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")

 		(signing-identifier "com.apple.facetimemessagestored")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.marco")
+		(signing-identifier "com.apple.asktod")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.MTLCompilerService")
+		(xpc-service-name "com.apple.AGXCompilerService*")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.AGXCompilerService*")
+		(xpc-service-name "com.apple.MTLCompilerService")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.dnssd.service")
+		(global-name "com.apple.nesessionmanager")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.trustd")
+		(global-name "com.apple.securityd")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.securityd")
+		(global-name "com.apple.trustd")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nesessionmanager")
+		(global-name "com.apple.dnssd.service")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.marco")
-		(signing-identifier "com.apple.Carousel")
+		(global-name "com.apple.medialibraryd.xpc")
+		(signing-identifier "com.apple.siriknowledged")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.cloudd")
+		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(xpc-service-name "com.apple.ImageIOXPCService")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(require-any

 		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(xpc-service-name "com.apple.ImageIOXPCService")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.cloudd")
-		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.locationd.synchronous")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.spotlight.IndexDelegateAgent")
+		(global-name "com.apple.spotlight.IndexAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.spotlight.IndexAgent")
+		(global-name "com.apple.spotlight.IndexDelegateAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ABDatabaseDoctor")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(global-name "com.apple.accountsd.accountmanager")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.accountsd.accountmanager")
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.ABDatabaseDoctor")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.geoanalyticsd")
+		(require-any
+			(global-name "com.apple.geod")
+			(global-name "com.apple.nanomaps.xpc.GeoServices")
+		)
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+		(global-name "com.apple.geoanalyticsd")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(require-any
-			(global-name "com.apple.geod")
-			(global-name "com.apple.nanomaps.xpc.GeoServices")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+		(global-name "com.apple.iokit.powerdxpc")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "*")
+		(xpc-service-name "com.apple.*")
 		(require-any
-			(require-any
-				(signing-identifier "com.apple.InputUI")
-				(signing-identifier "com.apple.destinationd")
-				(signing-identifier "com.apple.donotdisturbd")
-				(signing-identifier "com.apple.locationpushd")
-				(signing-identifier "com.apple.symptomsd-diag")
-			)
-			(signing-identifier "com.apple.assistantd")
+			(signing-identifier "com.apple.InputUI")
+			(signing-identifier "com.apple.destinationd")
+			(signing-identifier "com.apple.donotdisturbd")
+			(signing-identifier "com.apple.locationpushd")
+			(signing-identifier "com.apple.symptomsd-diag")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.awdd")
+		(global-name "com.apple.FileCoordination")
 		(require-any
 			(require-all
-				(global-name "com.apple.awdd")
+				(global-name "com.apple.FileCoordination")
 				(signing-identifier "com.apple.nanophoned")
 			)
 			(signing-identifier "com.apple.tursd")

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.Carousel")
+		(xpc-service-name "*")
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(require-any
+				(signing-identifier "com.apple.InputUI")
+				(signing-identifier "com.apple.destinationd")
+				(signing-identifier "com.apple.donotdisturbd")
+				(signing-identifier "com.apple.locationpushd")
+				(signing-identifier "com.apple.symptomsd-diag")
+			)
+			(signing-identifier "com.apple.assistantd")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.*")
-		(signing-identifier "com.apple.assistantd")
+		(signing-identifier "com.apple.Carousel")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access")

 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(global-name "com.apple.PowerManagement.control")
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 		)
 	)
 )

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(signing-identifier "com.apple.usernotificationsd")

 (allow syscall-unix
 	(require-all
 		(syscall-number SYS_csrctl SYS_flock SYS_fsync SYS_ftruncate)
-		(signing-identifier "com.apple.nanophoned")
+		(signing-identifier "com.apple.tursd")
 	)
 )
 (allow syscall-unix

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow sysctl-read
+	(require-all
+		(require-any
+			(sysctl-name "kern.nisdomainname")
+			(sysctl-name "net.statistics")
+		)
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
 (allow sysctl-read
 	(require-all
 		(sysctl-name "net.routetable.*")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "net.statistics")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "kern.nisdomainname")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.network.client")
 			(%entitlement-is-bool-true "com.apple.security.network.server")

 
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
-		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(fsctl-command APFSIOC_GET_CLONE_INFO APFSIOC_GET_PURGEABLE_FILE_FLAGS)
+		(signing-identifier "com.apple.storagedatad")
 	)
 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_DIR_STATS)
+		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.network.client")
 			(%entitlement-is-bool-true "com.apple.security.network.server")

 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_CLONE_INFO APFSIOC_GET_PURGEABLE_FILE_FLAGS)
-		(signing-identifier "com.apple.storagedatad")
+		(fsctl-command APFSIOC_GET_DIR_STATS)
+		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
 (allow system-fsctl

 		(signing-identifier "com.apple.managedassetsd")
 	)
 )
+(allow system-fsctl
+	(require-all
+		(fsctl-command APFSIOC_MAINTAIN_DIR_STATS APFSIOC_MARK_PURGEABLE)
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow system-fsctl
+	(require-all
+		(fsctl-command APFSIOC_GET_PURGEABLE_FILE_FLAGS)
+		(require-any
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.FileProviderDaemon.FPCKService")
+		)
+	)
+)
 (allow system-fsctl
 	(require-all
 		(fsctl-command (_IO "h" 31) HFSIOC_TRANSFER_DOCUMENT_ID)

 			APFSIOC_DOC_ID_TO_FILE_ID
 			APFSIOC_GET_DIR_STATS_EXT
 			APFSIOC_GET_PURGEABLE_FILE_FLAGS
-			APFSIOC_MAINTAIN_DIR_STATS
 			APFSIOC_PURGEABLE_GET_FILE_INFO)
 		(signing-identifier "com.apple.FileProviderDaemon.FPCKService")
 	)
 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command
-			APFSIOC_GET_DIR_STATS_EXT
-			APFSIOC_MAINTAIN_DIR_STATS
-			APFSIOC_MARK_PURGEABLE)
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow system-fsctl
-	(require-all
-		(fsctl-command APFSIOC_GET_PURGEABLE_FILE_FLAGS)
+		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
 		(require-any
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.FileProviderDaemon.FPCKService")
+			(require-all
+				(fsctl-command APFSIOC_MAINTAIN_DIR_STATS)
+				(signing-identifier "com.apple.FileProviderDaemon.FPCKService")
+			)
+			(signing-identifier "com.apple.mediaplaybackd")
 		)
 	)
 )

 
 (allow system-kas-info
 	(require-all
-		(system-attribute internal-build)
 		(system-attribute developer-mode)
+		(system-attribute internal-build)
 		(kas-info-selector KAS_INFO_KERNEL_TEXT_SLIDE_SELECTOR)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)

 		)
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.homesharing")
-		(signing-identifier "com.apple.siriknowledged")
-	)
-)
 (allow user-preference-read
 	(require-all
 		(preference-domain "com.apple.CFNetwork")
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.CloudKit")
-		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.avfoundation")
-		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-	)
-)
 (allow user-preference-read
 	(require-all
 		(preference-domain "com.apple.coreaudio")

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.corevideo")
+		(preference-domain "com.apple.avfoundation")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.Metal")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(preference-domain "com.apple.itunesstored")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.itunesstored")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
+		(preference-domain "com.apple.CloudKit")
+		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.corevideo")
+		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.logging")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(preference-domain "com.apple.conference")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.Metal")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
 (allow user-preference-read

 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.logging")
-		(signing-identifier "com.apple.facetimemessagestored")
-	)
-)
-(allow user-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(require-any
-			(preference-domain "com.apple.AOSNotification.public.notbackedup")
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.DataMigration")
-			(preference-domain "com.apple.PeoplePicker")
-			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
-			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
-			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
-			(require-all
-				(preference-domain "com.apple.CoreDuet")
-				(process-attribute is-apple-signed-executable)
-			)
-		)
-	)
-)
 (allow user-preference-read
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 		)
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.mobileipod")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.GEO")
-			(preference-domain "com.apple.locationd")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.marco")
-		(require-any
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.conference")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.internal.livtipsd")
-				(signing-identifier "com.apple.usernotificationsd")
-			)
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-		)
-	)
-)
 (allow user-preference-read
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
-		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
-		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.ids")
-		(signing-identifier "com.apple.facetimemessagestored")
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.medialibrary")
-		(signing-identifier "com.apple.siriknowledged")
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.MobileAsset")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(signing-identifier "com.apple.internal.livtipsd")
 		(require-any
 			(preference-domain "com.apple.logging")
 			(preference-domain "com.apple.marco")

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.companionsync")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 		(require-any
-			(signing-identifier "com.apple.nanophoned")
-			(signing-identifier "com.apple.tursd")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
-		(signing-identifier "com.apple.usernotificationsd")
+		(preference-domain "com.apple.homesharing")
+		(signing-identifier "com.apple.siriknowledged")
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
+		(preference-domain "com.apple.MobileAsset")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.GEO")
+			(preference-domain "com.apple.locationd")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(signing-identifier "com.apple.internal.livtipsd")
+		(require-any
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")

 		)
 	)
 )
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.internal.livtipsd")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.companionsync")
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.medialibrary")
+		(signing-identifier "com.apple.siriknowledged")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.logging")
+		(require-any
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.conference")
+		(signing-identifier "com.apple.FTLivePhotoService")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.usernotificationsd")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.assistant.public")
+		(require-any
+			(signing-identifier "com.apple.corespeechd")
+			(signing-identifier "com.apple.speech.localspeechrecognition")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.FTLivePhotoService")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(preference-domain "com.apple.AOSNotification.public.notbackedup")
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.DataMigration")
+			(preference-domain "com.apple.PeoplePicker")
+			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
+			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
+			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+			(require-all
+				(preference-domain "com.apple.CoreDuet")
+				(process-attribute is-apple-signed-executable)
+			)
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.mobileipod")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(require-any
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
+		)
+	)
+)
 (allow user-preference-read
 	(require-any
 		(preference-domain "com.apple.NanoRegistry")

 		)
 	)
 )
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.homesharing")
-		(signing-identifier "com.apple.siriknowledged")
-	)
-)
 (allow managed-preference-read
 	(require-all
 		(preference-domain "com.apple.CFNetwork")
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.CloudKit")
-		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.avfoundation")
-		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-	)
-)
 (allow managed-preference-read
 	(require-all
 		(preference-domain "com.apple.coreaudio")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.corevideo")
+		(preference-domain "com.apple.avfoundation")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.Metal")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(preference-domain "com.apple.itunesstored")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
 	)
 )
 (allow managed-preference-read

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.itunesstored")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
+		(preference-domain "com.apple.CloudKit")
+		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.corevideo")
+		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow managed-preference-read

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.logging")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(preference-domain "com.apple.conference")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.Metal")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
 (allow managed-preference-read

 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.logging")
-		(signing-identifier "com.apple.facetimemessagestored")
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(require-any
-			(preference-domain "com.apple.AOSNotification.public.notbackedup")
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.DataMigration")
-			(preference-domain "com.apple.PeoplePicker")
-			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
-			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
-			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
-			(require-all
-				(preference-domain "com.apple.CoreDuet")
-				(process-attribute is-apple-signed-executable)
-			)
-		)
-	)
-)
 (allow managed-preference-read
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 		)
 	)
 )
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.mobileipod")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(preference-domain "com.apple.AppSupport")
-			(preference-domain "com.apple.GEO")
-			(preference-domain "com.apple.locationd")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.marco")
-		(require-any
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.conference")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.internal.livtipsd")
-				(signing-identifier "com.apple.usernotificationsd")
-			)
-			(signing-identifier "com.apple.Carousel")
-			(signing-identifier "com.apple.FTLivePhotoService")
-			(signing-identifier "com.apple.announced")
-			(signing-identifier "com.apple.asktod")
-			(signing-identifier "com.apple.facetimemessagestored")
-		)
-	)
-)
 (allow managed-preference-read
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
-		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
-		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.ids")
-		(signing-identifier "com.apple.facetimemessagestored")
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.medialibrary")
-		(signing-identifier "com.apple.siriknowledged")
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.MobileAsset")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(signing-identifier "com.apple.internal.livtipsd")
 		(require-any
 			(preference-domain "com.apple.logging")
 			(preference-domain "com.apple.marco")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.companionsync")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 		(require-any
-			(signing-identifier "com.apple.nanophoned")
-			(signing-identifier "com.apple.tursd")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
-		(signing-identifier "com.apple.usernotificationsd")
+		(preference-domain "com.apple.homesharing")
+		(signing-identifier "com.apple.siriknowledged")
 	)
 )
 (allow managed-preference-read

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
+		(preference-domain "com.apple.MobileAsset")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.GEO")
+			(preference-domain "com.apple.locationd")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(signing-identifier "com.apple.internal.livtipsd")
+		(require-any
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")

 		)
 	)
 )
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.internal.livtipsd")
+				(signing-identifier "com.apple.usernotificationsd")
+			)
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.companionsync")
+		(require-any
+			(signing-identifier "com.apple.nanophoned")
+			(signing-identifier "com.apple.tursd")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.medialibrary")
+		(signing-identifier "com.apple.siriknowledged")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.logging")
+		(require-any
+			(signing-identifier "com.apple.Carousel")
+			(signing-identifier "com.apple.FTLivePhotoService")
+			(signing-identifier "com.apple.announced")
+			(signing-identifier "com.apple.asktod")
+			(signing-identifier "com.apple.facetimemessagestored")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.conference")
+		(signing-identifier "com.apple.FTLivePhotoService")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.usernotificationsd")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.assistant.public")
+		(require-any
+			(signing-identifier "com.apple.corespeechd")
+			(signing-identifier "com.apple.speech.localspeechrecognition")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.marco")
+		(signing-identifier "com.apple.FTLivePhotoService")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(preference-domain "com.apple.AOSNotification.public.notbackedup")
+			(preference-domain "com.apple.AppSupport")
+			(preference-domain "com.apple.DataMigration")
+			(preference-domain "com.apple.PeoplePicker")
+			(preference-domain "com.apple.icloud.findmydeviced.postwipe")
+			(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
+			(preference-domain "com.apple.iokit.IOMobileGraphicsFamily")
+			(require-all
+				(preference-domain "com.apple.CoreDuet")
+				(process-attribute is-apple-signed-executable)
+			)
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.mobileipod")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(require-any
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
+		)
+	)
+)
 (allow managed-preference-read
 	(require-any
 		(preference-domain "com.apple.NanoRegistry")
```
