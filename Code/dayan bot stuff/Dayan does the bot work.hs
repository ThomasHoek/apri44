import Control.Concurrent


promptLine :: String -> IO String
promptLine prompt = do
    putStr prompt
    getLine

main :: IO()
main = do     
    putStrLn "Dayan, does the bot work?"
    line <- promptLine ""         -- line :: String
    if line == "No" || line  == "no"
        then putStrLn "WHY IS THE BOT NOT SHOWING ANY PICTURES\nfucking niggers obviously"
        else putStrLn "Don't Complain"
    
    threadDelay 2000000
    
    