#pragma once
#include"../models/Song.hpp"
#include"../device/IAudioOutputDevice.hpp"
#include<string>
#include<iostream>

using namespace std;

class AudioEngine{
    private:
        Song*currentSong;
        bool songIsPaused;
    public:
        AudioEngine(){
            currentSong=nullptr;
            songIsPaused=false; 
        }
        string getCurrentSongTitle() const{
            if(currentSong){
                return currentSong->getTitle();
            }
            return "";
        }
        bool isPause()const{
            return songIsPaused;
        }
        void play(IAudioOutputDevice*add, Song*song){
            if(song==nullptr)throw runtime_error("Cannot play a null song");
        }
};